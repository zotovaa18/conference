def validate_file1_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.doc', '.docx', '.rtf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Необходим файл в одном из следующих форматов: *.doc, *.docx, *.rtf.')


def validate_file2_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Необходим файл в формате *.pdf.')