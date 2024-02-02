#include <Python.h>

void print_python_string(PyObject *p) {
    PyCompactUnicodeObject *compact_unicode;
    PyASCIIObject *ascii_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        ascii_str = (PyASCIIObject *)p;
        printf("  type: compact ascii\n");
        printf("  length: %zd\n", ascii_str->length);
        printf("  value: %s\n", PyUnicode_AsUTF8(p));
    } else if (PyUnicode_IS_COMPACT(p)) {
        compact_unicode = (PyCompactUnicodeObject *)p;
        printf("  type: compact unicode object\n");
        printf("  length: %zd\n", compact_unicode->length);
        printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
    } else {
        printf("  [ERROR] Unsupported String Object\n");
    }
}


