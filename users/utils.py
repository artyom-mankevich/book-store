def user_directory_path(instance, filename):
    """Returns MEDIA_ROOT/uploads/user_username/filename"""
    return 'uploads/{0}/{1}'.format(instance.username, filename)