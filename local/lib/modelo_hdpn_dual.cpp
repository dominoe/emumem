#include "emumem_funcs.hpp"

#define INCPIN_1	0
#define UDPIN_1		1
#define CSPIN_1		4

#define INCPIN_2	2
#define UDPIN_2		6
#define CSPIN_2		5

void modelo_hdpn_dual(double w_1 = 0.5, 
				 double eta_1_m = 1.0,
				 double eta_1_p = 1.0, 
				 double delta_1_m = 1.0,
				 double delta_1_p = 1.0, 
				 double t0_1 = 1.0, 
				 double v0_1 = 1.0, 
				 double alpha_1 = 1.0, 
				 double Rs_1 = 100.0, 
				 double I0min_1 = 1.0, 
				 double I0max_1 = 1.0, 
				 uint8_t lvl_on_1 = 0, 
				 uint8_t lvl_off_1 = 99,
				 double w_2 = 0.5, 
				 double eta_2_m = 1.0, 
				 double eta_2_p = 1.0,
				 double delta_2_m = 1.0,
				 double delta_2_p= 1.0, 
				 double t0_2 = 1.0, 
				 double v0_2 = 1.0, 
				 double alpha_2 = 1.0, 
				 double Rs_2 = 100.0, 
				 double I0min_2 = 1.0, 
				 double I0max_2 = 1.0, 
				 uint8_t lvl_on_2 = 0, 
				 uint8_t lvl_off_2 = 99, 
				 int n_meds = 100)
{
	//const uint8_t lvl_off	= 80; //20;
	//const uint8_t lvl_on	= 2; //10;
	const uint8_t lvl_diff_1	= lvl_off_1-lvl_on_1;
	const uint8_t lvl_diff_2	= lvl_off_2-lvl_on_2;

	const double v_off = 2.505; // Offset de voltaje
	//const double v_att = 0.6734; // Atenuación de voltaje
	const double v_att = 1;
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;
		
	uint8_t r_level_1 = lvl_off_1 - (uint8_t)rint(w_1*((double)lvl_diff_1));
	uint8_t r_level_2 = lvl_off_2 - (uint8_t)rint(w_2*((double)lvl_diff_2));
	
	struct timespec gettime_now;
	double dt_1, t_prev_1, t_cur_1;
	double dt_2, t_prev_2, t_cur_2;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu_01 = new DigiPot(INCPIN_1, UDPIN_1, CSPIN_1);
	emu_01->increase(lvl_off_1);
	emu_01->set(r_level_1);
	
	DigiPot* emu_02 = new DigiPot(INCPIN_2, UDPIN_2, CSPIN_2);
	emu_02->increase(lvl_off_2);
	emu_02->set(r_level_2);
	
	// MEDICIÓN DE TIEMPO DE INTEGRACIÓN O w (OPCIONAL)
	int i = 0;
	double* ret_dt_1 = new double[n_meds];
	//double * ret_w_1 = new double[n_meds];
	//double * ret_v_1 = new double[n_meds];
	//double * ret_I_1 = new double[n_meds];
	double* ret_dt_2 = new double[n_meds];
	//double * ret_w_2 = new double[n_meds];
	//double * ret_v_2 = new double[n_meds];
	//double * ret_I_2 = new double[n_meds];

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur_1 = gettime_now.tv_nsec;

	double v_1 = mcp3008_read(0)*v_slope + v_intercept;
	double lambda_1 = w_1; // Para que no se mueva al principio (condición inicial).
	double constante_1 = 1.0e-9/t0_1;
	double R_1;
	
	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur_2 = gettime_now.tv_nsec;
	
	double v_2 = mcp3008_read(1)*v_slope + v_intercept;
	double lambda_2 = w_2; // Para que no se mueva al principio (condición inicial).
	double constante_2 = 1.0e-9/t0_2;
	double R_2;

	while(1)
	{
		
		// MEMRISTOR 1
		t_prev_1 = t_cur_1;
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		t_cur_1 = gettime_now.tv_nsec;
		dt_1 = t_cur_1 - t_prev_1;
		if (dt_1<0.0) dt_1 += 1.0e+9;

		v_1 = mcp3008_read(0)*v_slope + v_intercept;
		lambda_1 = LAMBDA(v_1,lambda_1,eta_1_m,eta_1_p,delta_1_m,delta_1_p);
		w_1 +=  (dt_1*constante_1*(lambda_1 - w_1)*exp(abs(v_1)/((double)v0_1)));

		if(w_1<0.0) w_1 = 0.0;
		else if(w_1>1.0) w_1 = 1.0;

		R_1 = v_1 / I_nonlinear(v_1,I0min_1+ w_1*(I0max_1-I0min_1),alpha_1,Rs_1);

		r_level_1 = (uint8_t)rint((R_1-RES_MIN)/QUANT_RES);

		if (r_level_1 < lvl_on_1) r_level_1 = lvl_on_1;
		if (r_level_1 > lvl_off_1) r_level_1 = lvl_off_1;

		emu_01->set(r_level_1);
		
		// MEMRISTOR 2
		
		t_prev_2 = t_cur_2;
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		t_cur_2 = gettime_now.tv_nsec;
		dt_2 = t_cur_2 - t_prev_2;
		if (dt_2<0.0) dt_2 += 1.0e+9;

		v_2 = mcp3008_read(1)*v_slope + v_intercept;
		lambda_2 = LAMBDA(v_2,lambda_2,eta_2_m,eta_2_p,delta_2_m,delta_2_p);
		w_2 +=  (dt_2*constante_2*(lambda_2 - w_2)*exp(abs(v_2)/((double)v0_2)));

		if(w_2<0.0) w_2 = 0.0;
		else if(w_2>1.0) w_2 = 1.0;

		R_2 = v_2 / I_nonlinear(v_2,I0min_2+ w_2*(I0max_2-I0min_2),alpha_2,Rs_2);

		r_level_2 = (uint8_t)rint((R_2-RES_MIN)/QUANT_RES);

		if (r_level_2 < lvl_on_2) r_level_2 = lvl_on_2;
		if (r_level_2 > lvl_off_2) r_level_2 = lvl_off_2;

		emu_02->set(r_level_2);
		
		//OPCIONAL: DESCOMENTAR PARA CALCULAR TIEMPO DE INTEGRACIÓN
		//time_dt[time_i++] = dt;
		//if(time_total<time_max)
		//{for(int i=0; i<time_i;i++) std::cout << time_dt[i] << "\t"; break;}

		// MEDICIÓN DE w, tiempo de integración, etc. (DESCOMENTAR EN NECESIDAD)
		//ret_dt_1[i] = dt_1;
		//ret_w_1[i] = w_1;
		//ret_v_1[i] = v_1;
		//ret_I_1[i] = I_nonlinear(v_1,I0min_1+ w_1*(I0max_1-I0min_1),alpha_1,Rs_1);
		//if(++i>n_meds) break;
		
		//ret_dt_2[i] = dt_2;
		//ret_w_2[i] = w_2;
		//ret_v_2[i] = v_2;
		//ret_I_2[i] = I_nonlinear(v_2,I0min_2+ w_2*(I0max_2-I0min_2),alpha_2,Rs_2);
		//if(++i>n_meds) break;
	}
	// IMPRESIÓN DE TIEMPOS DE INTEGRACIÓN o w
	//for(int i=0; i<n_meds;i++) std::cout << ret_dt_1[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_w_1[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_v_1[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_I_1[i] << "\t";
	
	//for(int i=0; i<n_meds;i++) std::cout << ret_dt_2[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_w_2[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_v_2[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_I_2[i] << "\t";
}
