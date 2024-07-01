from src.auth.piccolo_app import APP_CONFIG as auth_conf
from src.course.piccolo_app import APP_CONFIG as course_conf
# from src.admin.piccolo_app import APP_CONFIG as admin_conf
# from src.student.piccolo_app import APP_CONFIG as student_conf
# from src.course.piccolo_app import APP_CONFIG as course_conf


APP_CONFIG = []
APP_CONFIG.extend(auth_conf.table_classes)
APP_CONFIG.extend(course_conf.table_classes)
# APP_CONFIG.extend(admin_conf.table_classes)
# APP_CONFIG.extend(student_conf.table_classes)
# APP_CONFIG.extend(course_conf.table_classes)
