#include <Python.h>

/**
 * print_python_list_info - Python basic info lists
 * @p - pyobj list
 */
void print_python_list_info(PyObject *p)
{
	int sz, a_loc, a;
	PyObject *obj;

	sz = Py_SIZE(p);
	a_loc = ((PyListObject *)p) -> allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", a_loc);

	for (a = 0; a < sz; a++)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj) -> tp_name);
	}
}
