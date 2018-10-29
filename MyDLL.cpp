/*! \generate dll for windows with default _cdecl calling convention
*/

extern "C" {
	_declspec(dllexport) int add(int a, int b);
	_declspec(dllexport) int divide(int a, int b, int* c);
	_declspec(dllexport) double avg(double* dptr, int len);
}

_declspec(dllexport) int add(int a, int b)
{
	return a + b;
}

_declspec(dllexport) int divide(int a, int b, int* c)
{
	int rst = a / b;
	*c = a % b;
	return rst;
}

_declspec(dllexport) double avg(double* dptr, int len)
{
	double total = 0.0;
	for(int i = 0; i < len; ++i)
	{
		total += dptr[i];
	}
	return total / len;
}
