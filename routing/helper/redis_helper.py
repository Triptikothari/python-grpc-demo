from routing.shared.utility.redis import RedisAccessor

class RedisHelper:

    @staticmethod
    def set_initiate_merchant__submerchant_data(merchant_key, submerchant_key, value):
        try:
            redis_data = RedisAccessor.setData(key="initiate_merchant_config__" + str(merchant_key)+ "__submerchant_config__"+ str(submerchant_key), value=value)
            return True
        except Exception as e:
            return str(e)
        
    
    @staticmethod
    def set_initiate_merchant_data(merchant_key, value):
        try:
            redis_data = RedisAccessor.setData(key="initiate_merchant_config__" + str(merchant_key), value=value)
            return True
        except Exception as e:
            return str(e)