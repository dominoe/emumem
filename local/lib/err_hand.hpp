#pragma once

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>

//////////////////////////////////////////////////
// PROTOTIPOS ////////////////////////////////////
//////////////////////////////////////////////////

void exit_success(std::string);
void exit_failure(std::string);
void flush_message(std::string);
bool try_subroutine(std::string, int);
static struct { int argc; std::string name; std::vector<std::string> argv; } Subroutine;

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
