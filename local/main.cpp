//////////////////////////////////////////////////
// EMUMEM LOCAL (2019-05-23) /////////////////////
//////////////////////////////////////////////////

#include "lib/err_hand.hpp"
#include "lib/emumem_funcs.hpp"

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
	else if(try_subroutine("modelo_hp",3)) modelo_hp(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stoi(Subroutine.argv[2]));
	else if(try_subroutine("modelo_hist",5)) modelo_hist(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]), std::stod(Subroutine.argv[2]),
														std::stod(Subroutine.argv[3]), std::stod(Subroutine.argv[4]));
	else exit_failure("No se ha designado ningún programa correctamente.");
	
	//exit_success(0);
}
