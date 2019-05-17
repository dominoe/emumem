//////////////////////////////////////////////////
// EMUMEM LOCAL (2019-04-27) /////////////////////
//////////////////////////////////////////////////

#include "header.hpp"

//////////////////////////////////////////////////
// MAIN Y SUBRUTINAS /////////////////////////////
//////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	if(argc==1) exit_failure("Error Fatal: El modo de uso es 'main <comando>'");
	
	Subroutine.name = argv[1];
	Subroutine.argc =  argc-2;
	std::copy(argv+2, argv+argc, std::back_inserter(Subroutine.argv));

	if(try_subroutine("reset",0)) reset();
	if(try_subroutine("inc_resistance",1)) inc(std::stof(Subroutine.argv[0]));
	if(try_subroutine("dec_resistance",1)) dec(std::stof(Subroutine.argv[0]));
	if(try_subroutine("set_resistance",1)) set_resistance(std::stof(Subroutine.argv[0]));
	if(try_subroutine("adq_mcp",3)) mcp3008_data(std::stoi(Subroutine.argv[0]), std::stoi(Subroutine.argv[1]), std::stoi(Subroutine.argv[2]));
	if(try_subroutine("modelo_hp",2)) modelo_hp(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]));

	exit_success("El programa ha finalizado correctamente");
}