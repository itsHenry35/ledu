@echo off
::提权
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )

::设置编码，使中文正常显示
chcp 65001

::确认是否安装
echo 是否确认安装Python?
pause

::定位到实际所在目录
cd /d %~dp0

::安装python
python_install /Quiet SimpleInstall=1 InstallAllUsers=1 PrependPath=1

::设置pypi镜像，国内pypi太难了
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple 

::安装三方库
pip install -r requirements.txt

echo 安装完成！
pause