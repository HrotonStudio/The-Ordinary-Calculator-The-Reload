from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

class RSAUtil:
    @staticmethod
    def generate_keys():
        """生成RSA密钥对"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt(message: str, public_key) -> str:
        """使用公钥加密字符串"""
        encrypted = public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(encrypted).decode('utf-8')

    @staticmethod
    def decrypt(encrypted: str, private_key) -> str:
        """使用私钥解密字符串"""
        decoded = base64.b64decode(encrypted)
        original = private_key.decrypt(
            decoded,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return original.decode('utf-8')

    @staticmethod
    def save_private_key(private_key, filename: str):
        """保存私钥到PEM文件"""
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(filename, 'wb') as f:
            f.write(pem)

    @staticmethod
    def save_public_key(public_key, filename: str):
        """保存公钥到PEM文件"""
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(filename, 'wb') as f:
            f.write(pem)

    @staticmethod
    def load_private_key(filename: str):
        """从PEM文件加载私钥"""
        with open(filename, 'rb') as f:
            pem = f.read()
        return serialization.load_pem_private_key(
            pem,
            password=None,
            backend=default_backend()
        )

    @staticmethod
    def load_public_key(filename: str):
        """从PEM文件加载公钥"""
        with open(filename, 'rb') as f:
            pem = f.read()
        return serialization.load_pem_public_key(
            pem,
            backend=default_backend()
        )

if __name__ == "__main__":
    # 生成密钥对
    private_key, public_key = RSAUtil.generate_keys()
    
    # 保存密钥
    RSAUtil.save_private_key(private_key, 'private_key.pem')
    RSAUtil.save_public_key(public_key, 'public_key.pem')
    
    # 加密演示
    message = "Hello RSA加密世界!"
    encrypted = RSAUtil.encrypt(message, public_key)
    print(f"加密结果: {encrypted}")
    
    # 解密演示
    decrypted = RSAUtil.decrypt(encrypted, private_key)
    print(f"解密结果: {decrypted}")