import  logging

format_dict = {
    'file_format': logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s -- %(pathname)s' ),
    'Stream_format': logging.Formatter('%(levelname)s -- %(message)s -- %(pathname)s')
}


class Log(object):
    '''
    logger：日志名__name__
    log_file_Name:日志的文件名
    '''
    def __init__(self,log_file_Name,logger):
        #创建logging对象
        self.log = logging.getLogger(logger)
        self.log.setLevel(logging.INFO)

        Fhandler = logging.FileHandler(log_file_Name,mode='w',encoding='utf-8')
        Shandler = logging.StreamHandler()

        f_format = format_dict['file_format']
        s_format = format_dict['Stream_format']
        Fhandler.setFormatter(f_format)
        Shandler.setFormatter(s_format)

        self.log.addHandler(Fhandler)
        self.log.addHandler(Shandler)

    def my_deubg(self,str_debug):
        self.log.debug(str_debug)

    def my_info(self,str_info):
        self.log.info(str_info)

    def my_waring(self,str_waring):
        self.log.warning(str_waring)

    def my_error(self,str_error):
        self.log.error(str_error)

    def my_critical(self,str_critical):
        self.log.critical(str_critical)


    def getLog(self):
        return self.log





