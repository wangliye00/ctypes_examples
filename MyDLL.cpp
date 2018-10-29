/*! \generate dll for windows with default _cdecl calling convention
*/

extern "C" {
	_declspec(dllexport) int add(int a, int b);
}

_declspec(dllexport) int add(int a, int b){
  return a + b;
}
