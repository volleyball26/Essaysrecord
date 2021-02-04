git init        创建一个本地仓库
git remote      管理与远程仓库通信配置
    - 设置项目 URL: `git remote add origin https://github.com/vollxxxxall.git`
git config --global user.name ''
git config --global user.email ''
git status      查看当前仓库状态
git add ./        将文件添加到 “暂存区”
git commit      将暂存区中的文件提交到 “本地仓库”
git push origin master
git diff        差异对比

git checkout    代码还原 / 代码回滚
    - 本地代码还原: `git checkout ./`
    - 代码回滚: `git checkout 8aecffadb2c1364e54912591e9323f08e1268562`
    - 快速回滚上一个版本: `git checkout HEAD^`

git reset       取消文件的暂存状态

git log         查看提交日志
    - `--stat `
    - `--graph`
    - `-p`

git config --global user.name ''
git config --global user.email ''

git remote      管理与远程仓库通信配置
    - 设置项目 URL: `git remote add origin https://github.com/vollxxxxll.git`
    - 修改项目 URL: ` git remote set-url origin git@github.com:volxxxxall.git

git push        将 “本地仓库” 的更新推送到 “远程仓库”
git pull        将 “远程仓库” 的更新拉取到 “本地仓库”

git clone       将 “远程仓库” 完整的克隆到本地




Git提交

1.生成密钥，会在.ssh目录下生成2个密钥文件
ssh-keygen -t rsa -C "your_email"

2.复制公钥
cat ~/.ssh/id_rsa.pub

3.在github后台添加公钥
