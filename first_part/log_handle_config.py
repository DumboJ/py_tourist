import logging

# 创建logging
log = logging.getLogger('handler_log')
# 设置级别
log.setLevel(logging.DEBUG)
# 创建handler
console_log = logging.StreamHandler()
console_log.setLevel(logging.WARNING)
file_log = logging.FileHandler('handler_log.log')
file_log.setLevel(logging.INFO)

console_formatter = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-%(message)s')
file_formatter = logging.Formatter('%(asctime)s-%(filename)s-%(lineno)-%(levelname)s-%(message)s')

console_log.setFormatter(console_formatter)
file_log.setFormatter(file_formatter)

log.addHandler(console_log)
log.addHandler(file_log)

