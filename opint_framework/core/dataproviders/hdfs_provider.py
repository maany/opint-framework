from .base import BaseLoader
from pyspark.sql import SparkSession
import traceback


class HDFSLoader(BaseLoader):
    """
        Base data provider (used to load data from external sources)
    """

    def pull_hdfs_json(self, path, spark):
        try:
            return spark.read.json(path)
        except Exception as e:
            print('Error loading data from', path, e)
            traceback.print_tb(e.__traceback__)

    def pull_hdfs_dir(self, path, spark):
        try:
            fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration())
            list_status = fs.listStatus(spark._jvm.org.apache.hadoop.fs.Path(path))
            ret = []
            for file in [file.getPath().getName() for file in list_status]:
                ret.append(self.pull_hdfs_json(path+file, spark))
            return ret
        except Exception as e:
            print('Error listing files for ', path, e)

    @classmethod
    def fetch_data(cls, **kwargs):
        """
        Makes the connection to external source and fetches the data
        To be overwritten by parent

        :return: (data fetched from source)
        """
        spark = SparkSession.builder.master(**kwargs.get('spark_master'))\
            .appName(**kwargs.get('spark_name')).getOrCreate()
        if kwargs.get('type') == 'JSON':
            if kwargs.get('path'):
                return cls.pull_hdfs_dir(kwargs.get('path'), spark)
            elif kwargs.get('file'):
                return cls.pull_hdfs_json(kwargs.get('file'), spark)
        return None
