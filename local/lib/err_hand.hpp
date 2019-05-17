#pragma once

//////////////////////////////////////////////////
// CONTROL DE ERRORES ////////////////////////////
//////////////////////////////////////////////////

void flush_message(std::string message) {
	std::cout << message << std::endl;
}

void exit_failure(std::string message) {
	flush_message(message);
	exit(EXIT_FAILURE);
}

void exit_success(std::string message) {
	flush_message(message);
	exit(EXIT_SUCCESS);
}

bool try_subroutine(std::string name, int argc) {
	if (name.compare(Subroutine.name) != 0) return false;
	if (argc != Subroutine.argc) exit_success("Error Fatal: La subrutina llamada debe tener " + std::to_string(argc) + " argumentos propios.");
	return true;
}