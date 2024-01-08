#include <Python.h>
#include <stdio.h>



void print_python_list_info(PyObject *p)
{
	long int list_size, list_alloc, i;
	PyObject *list_item;

	list_size = PyList_Size(p);
	list_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %li\n", list_alloc);

	for (i = 0; i < list_size; i++)
	{
		list_item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(list_item)->tp_name);
	}
}
