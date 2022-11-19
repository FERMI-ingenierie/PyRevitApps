# # -*- coding: UTF-8 -*-
#
# from functools import wraps
# from Autodesk.Revit.Exceptions import InvalidOperationException
#
# from pyrevit.forms import ProgressBar
#
# def progressbar(title = "", maxvalue = 1, indeterminate = False,cancellable = False, step = 1):
#     def wrap(f):
#         @wraps(f)
#         def wrapped_f(*args) :
#             title = title
#             maxvalue = maxvalue
#
#             with ProgressBar() as pb:
#                 max = maxvalue
#                 maxvalue = maxvalue
#                 pb.max_value = maxvalue
#
#             try:
#                 t = Transaction(doc, transaction_name)
#                 t.Start()
#             except InvalidOperationException as errmsg:
#                 print('Transaciton Error: {}'.format(errmsg))
#                 return_value = f(*args)
#
#             else:
#                 return_value = f(*args)
#                 t.Commit()
#
#
#
#
#             return return_value
#         return wrapped_f
#     return wrap
#
#
# import functools
# def decorator(title = "", maxvalue = 1, indeterminate = False,cancellable = False, step = 1.):
#
#     def _decorate(function):
#         @functools.wraps(function)
#         def wrapped_function(*args, **kwargs):
#             # _title = title
#             _maxvalue = maxvalue
#             _indeterminate = indeterminate
#             _cancellable = cancellable
#             _step = step
#             with ProgressBar(title=title,
#                              maxvalue=maxvalue,
#                              indeterminate=indeterminate,
#                              cancellable = cancellable,
#                              step=step) as pb:
#                 count = 1
#
#         return wrapped_function
#
#     if original_function:
#         return _decorate(original_function)
#
#     return _decorate
#
# #Example
# @progressbar('Create Text')
# def create_text(view, text, point, align):
#     baseVec = XYZ.BasisX
#     upVec = XYZ.BasisZ
#     text_size = 10
#     text_length = 0.5
#     text = str(text)
#     align_options = {'left': TextAlignFlags.TEF_ALIGN_LEFT |
#                              TextAlignFlags.TEF_ALIGN_MIDDLE,
#                      'right': TextAlignFlags.TEF_ALIGN_RIGHT |
#                              TextAlignFlags.TEF_ALIGN_MIDDLE
#                      }
#
#     text_element = doc.Create.NewTextNote(view, point, baseVec, upVec, text_length,
#                                           align_options[align], text)