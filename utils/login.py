import customtkinter as ctk
import os, sys
from tkinter import messagebox
from src.settings import IsHaveKey
from src.base import Base
try:
    import utils.lock.rsa_lock as rsa_lock
    import utils.lock.md5_lock as md5_lock
except:
    import lock.rsa_lock as rsa_lock
    import lock.md5_lock as md5_lock

# 设置界面主题
ctk.set_appearance_mode("System")  # 可选 "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # 可选 "blue", "green", "dark-blue"

def create_key():
    Base.log("I", "创建密钥对", "login.create_key")
    users_private_key, users_public_key = rsa_lock.RSAUtil.generate_keys()
    password_private_key, password_public_key = rsa_lock.RSAUtil.generate_keys()
    rsa_lock.RSAUtil.save_private_key(users_private_key, "users_private_key.pem")
    rsa_lock.RSAUtil.save_public_key(users_public_key, "users_public_key.pem")
    rsa_lock.RSAUtil.save_private_key(password_private_key, "password_private_key.pem")
    rsa_lock.RSAUtil.save_public_key(password_public_key, "password_public_key.pem")
    open("users.ncw", "w", encoding="utf-8")
    with open("text\\settings.ini", "r", encoding="utf-8") as f:
        fff = f.read()
        fff.replace("IsHaveKey=False", "IsHaveKey=True")
    with open("text\\settings.ini", "w", encoding="utf-8") as f:
        f.write(fff)

def login():
    window = ctk.ctk_tk.CTk()
    window.title("登录")
    window.geometry("300x200")
    def close():
        os.system("taskkill /im python.exe /f")
    window.protocol("WM_DELETE_WINDOW", close)
    ctk.CTkLabel(window, text='你好',font=('Arial', 16)).grid(row=0, column=1)
    ctk.CTkLabel(window, text='用户名:', font=('Arial', 14)).grid(row=1, column=0)
    ctk.CTkLabel(window, text='密码:', font=('Arial', 14)).grid(row=2, column=0)
    var_usr_name = ctk.StringVar()
    var_usr_name.set('default')
    entry_usr_name = ctk.CTkEntry(window, textvariable=var_usr_name, font=('Arial', 14))
    entry_usr_name.grid(row=1, column=1)
    # 用户密码
    var_usr_pwd = ctk.StringVar()
    entry_usr_pwd = ctk.CTkEntry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
    entry_usr_pwd.grid(row=2, column=1)
    def usr_login():
        global usr_name
        Base.log("I", "正在登录", "login.Login")
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        try:
            with open("users.ncw", "r", encoding="utf-8") as f:
                users_private_key = rsa_lock.RSAUtil.load_private_key("users_private_key.pem")
                password_private_key = rsa_lock.RSAUtil.load_private_key("password_private_key.pem")
                users_str = f.readlines()
                users = []
                passwords = []
                dict_users = {}
                for i in users_str:
                    users.append(rsa_lock.RSAUtil.decrypt(i.split("#$%@1145141919810ncw@")[0].replace("\n", ""), users_private_key))
                    passwords.append(rsa_lock.RSAUtil.decrypt(i.split("#$%@1145141919810ncw@")[-1].replace("\n", ""), password_private_key))
                for u in users:
                    dict_users[u] = passwords[users.index(u)]
        except:
            create_key()
            is_sign_up = messagebox.askyesno('你好！ ', '你还没有注册账号，现在注册？')
            # 提示需不需要注册新用户
            if is_sign_up:
                usr_sign_up()
        if usr_name in dict_users:
            if usr_pwd == dict_users[usr_name]:
                messagebox.showinfo('欢迎！ ', '登录成功！')
                Base.log("I", "用户登录成功", "login.login")
                window.destroy()
            else:
                Base.log("E", "用户名或密码错误", "login.login")
        else:  # 如果发现用户名不存在
            is_sign_up = messagebox.askyesno('你好！ ', '你还没有注册账号，现在注册？')
            Base.log("E", "用户名不存在", "login.login")
            # 提示需不需要注册新用户
            if is_sign_up:
                usr_sign_up()

    def usr_sign_up():
        Base.log("I", "用户注册", "login.usr_sign_up")
        def sign_to():
            with open("users.ncw", "r", encoding="utf-8") as f:
                users_private_key = rsa_lock.RSAUtil.load_private_key("users_private_key.pem")
                users_str = f.readlines()
                users = []
                for i in users_str:
                    users.append(rsa_lock.RSAUtil.decrypt(i.split("#$%@1145141919810ncw@")[0].replace("\n", ""), users_private_key))
            password = new_pwd.get()
            confirm = new_pwd_confirm.get()
            username = new_name.get()
            users_public_key = rsa_lock.RSAUtil.load_public_key("users_public_key.pem")
            password_public_key = rsa_lock.RSAUtil.load_public_key("password_public_key.pem")
            # 验证逻辑
            if not all([username, password, confirm]):
                messagebox.showerror('Error', '用户名、密码、确认密码不能为空！')
                Base.log("E", "用户名、密码、确认密码不能为空", "login.Register")
                return
            if password != confirm:
                messagebox.showerror('Error', '两次输入密码必须一样！')
                Base.log("E", "两次输入的密码不一致", "login.Register")
                return
            if username in users:
                messagebox.showerror('Error', '这个用户已经注册过了！')
                Base.log("E", "用户名已存在", "login.Register")
                return
            encrypted_password = rsa_lock.RSAUtil.encrypt(password, password_public_key)
            encrypted_username = rsa_lock.RSAUtil.encrypt(username, users_public_key)
            save_info = encrypted_username + "#$%@1145141919810ncw@" + encrypted_password + "\n"
            with open("users.ncw", "a") as f:
                f.write(save_info)
            Base.log("I", "注册成功", "login.Register")
            window_sign_up.destroy()
        window_sign_up = ctk.CTkToplevel(window)
        window_sign_up.geometry('300x200')
        window_sign_up.title('注册窗口')
        new_name = ctk.StringVar()
        new_name.set('default')
        ctk.CTkLabel(window_sign_up, text='用户名: ').grid(row=0, column=0, padx=10, pady=10)
        entry_new_name = ctk.CTkEntry(window_sign_up, textvariable=new_name)
        entry_new_name.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        new_pwd = ctk.StringVar()
        ctk.CTkLabel(window_sign_up, text='密码: ').grid(row=1, column=0, padx=10, pady=10)
        entry_usr_pwd = ctk.CTkEntry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.grid(row=1, column=1, padx=10, pady=10)
        new_pwd_confirm = ctk.StringVar()
        ctk.CTkLabel(window_sign_up, text='再次输入密码: ').grid(row=2, column=0, padx=10, pady=10)
        entry_usr_pwd_confirm = ctk.CTkEntry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        btn_comfirm_sign_up = ctk.CTkButton(window_sign_up, text='注册', command=sign_to)
        btn_comfirm_sign_up.grid(row=3, column=1, padx=10, pady=10)
    btn_login = ctk.CTkButton(window, text='登录', command=usr_login, width=40)
    btn_login.grid(row=3, column=0, pady=10)
    btn_sign_up = ctk.CTkButton(window, text='注册', command=usr_sign_up, width=40)
    btn_sign_up.grid(row=3, column=1, pady=10)
    window.mainloop()
    return usr_name
