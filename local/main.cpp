//////////////////////////////////////////////////
// EMUMEM LOCAL (2019-05-23) /////////////////////
//////////////////////////////////////////////////

#include "lib/err_hand.hpp"
#include "lib/emumem_funcs.hpp"
#include "lib/modelo_hdpn_dual.cpp"

//////////////////////////////////////////////////
// MAIN Y SUBRUTINAS /////////////////////////////
//////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	if(argc==1) exit_failure("Error Fatal: El modo de uso es 'emumem <comando>'");
	
	Subroutine.name = argv[1];
	Subroutine.argc =  argc-2;
	std::copy(argv+2, argv+argc, std::back_inserter(Subroutine.argv));

	if(try_subroutine("reset",0)) reset();
	else if(try_subroutine("inc_resistance",1)) inc(std::stof(Subroutine.argv[0]));
	else if(try_subroutine("dec_resistance",1)) dec(std::stof(Subroutine.argv[0]));
	else if(try_subroutine("set_resistance",1)) set_resistance(std::stof(Subroutine.argv[0]));
	else if(try_subroutine("adq_mcp",3)) mcp3008_data(std::stoi(Subroutine.argv[0]), std::stoi(Subroutine.argv[1]), std::stoi(Subroutine.argv[2]));
	else if(try_subroutine("modelo_hp",5)) modelo_hp(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stoi(Subroutine.argv[2]), std::stoi(Subroutine.argv[3]), std::stoi(Subroutine.argv[4]));
	else if(try_subroutine("modelo_hdp",10)) modelo_hdp(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stod(Subroutine.argv[2]), std::stod(Subroutine.argv[3]), std::stod(Subroutine.argv[4]), std::stoi(Subroutine.argv[5]), std::stoi(Subroutine.argv[6]), std::stoi(Subroutine.argv[7]), std::stoi(Subroutine.argv[8]), std::stoi(Subroutine.argv[9]));
	else if(try_subroutine("modelo_hdpn",12)) modelo_hdpn(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stod(Subroutine.argv[2]), std::stod(Subroutine.argv[3]), std::stod(Subroutine.argv[4]), std::stod(Subroutine.argv[5]), std::stod(Subroutine.argv[6]), std::stod(Subroutine.argv[7]), std::stod(Subroutine.argv[8]), std::stoi(Subroutine.argv[9]), std::stoi(Subroutine.argv[10]), std::stoi(Subroutine.argv[11]));
	else if(try_subroutine("modelo_hdpn_dual",27)) modelo_hdpn_dual(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stod(Subroutine.argv[2]), std::stod(Subroutine.argv[3]), std::stod(Subroutine.argv[4]), std::stod(Subroutine.argv[5]), std::stod(Subroutine.argv[6]), std::stod(Subroutine.argv[7]), std::stod(Subroutine.argv[8]), std::stod(Subroutine.argv[9]), std::stod(Subroutine.argv[10]), std::stoi(Subroutine.argv[11]),
															   std::stoi(Subroutine.argv[12]), std::stod(Subroutine.argv[13]), std::stod(Subroutine.argv[14]), std::stod(Subroutine.argv[15]), std::stod(Subroutine.argv[16]), std::stod(Subroutine.argv[17]), std::stod(Subroutine.argv[18]), std::stod(Subroutine.argv[19]), std::stod(Subroutine.argv[20]), std::stod(Subroutine.argv[21]), std::stod(Subroutine.argv[22]),
															   std::stod(Subroutine.argv[23]), std::stoi(Subroutine.argv[24]), std::stoi(Subroutine.argv[25]), std::stoi(Subroutine.argv[26]));
	else exit_failure("No se ha designado ningún programa correctamente.");
	
	//exit_success(0);
}
