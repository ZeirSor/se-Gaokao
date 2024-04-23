**需求场景：**
为高考学子提供智能填报志愿和专业的系统，根据学生的高考科目、学科、分数排名以及大学录取的历史数据，推荐学生适合高校的录取概率。系统应具备地区和学校类型的筛选功能。

**系统功能要求：**

1. 智能填报志愿和专业推荐。
2. 根据学生的高考科目、学科、分数排名，推荐适合的高校及录取概率。
3. 地区和学校类型的筛选功能。
4. 模拟志愿填报功能。
5. 查看学校、专业历年在各地的招生情况。
6. 参考网站或竞品网站包括：
   - [掌上高考](https://www.gaokao.cn/)
   - AI高考志愿APP
   - "新高考通"模拟志愿填报工具
   - 高考U选
   - 夸克App-阿里智能信息事业群旗下夸克App
   - 手机智能填报志愿app排行榜TOP10下载 ([链接](https://www.pianwan.com/s/zj-562416))

# **高考志愿智能填报系统的需求分析和原型设计**

# **智慧选途**

## 1. 需求分析

### 1.1. 用户需求

1.1 **用户类型**

-   高考学生

1.2 **用户需求**

-   注册和登录账户
-   输入个人高考科目和分数信息
-   查看推荐的高校及专业
-   进行模拟志愿填报
-   查看历年各地学校招生情况
-   进行地区、学校类型等条件筛选
-   查看大学录取历史数据
-   获取高考相关资讯和建议

### 1.2. 系统功能需求

2.1 **用户管理**

-   注册账户
-   登录/登出
-   个人信息管理

2.2 **志愿填报**

-   输入高考科目和分数
-   推荐高校及专业
-   模拟志愿填报

2.3 **学校信息查询**

-   查看学校招生情况
-   查询专业历年录取数据
-   查看大学录取历史数据
-   获取高考相关资讯
-   根据地区、学校类型筛选高校

2.4 **专业信息查询**

-   筛选专业

## 2. 原型设计

> 建议，参考：80% 夸克高考+20%掌上高考

**只是草稿**

### 2.1. 登录/注册界面

-   提供注册和登录按钮
-   *****支持第三方登录（如微信、QQ）

### 2.2. 个人信息界面

-   展示用户基本信息
-   提供修改密码和注销账户选项

### 2.3. 首页

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060041266.png" alt="image-20231206004159119" style="zoom:40%;" />

#### 2.3.1. 批次分数线查询

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060046649.png" alt="image-20231206004652614" style="zoom:50%;" />



### 2.4. 志愿填报界面

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060043304.png" alt="image-20231206004357266" style="zoom:50%;" />

-   可以根据排序、地区、院校类型、专业类型选择
-   推荐等级分为 可冲击、较稳妥、可保底

### 2.5. 学校信息查询

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060045106.png" alt="image-20231206004511048" style="zoom:50%;" />


-   学校招生情况查询
-   专业历年录取数据查询
-   大学录取历史数据展示
-   高考相关资讯浏览
-   地区、学校类型、学校层次等条件筛选
-   收藏功能

### 2.6. 专业信息查询

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312011555401.png" alt="image-20231201155546352" style="zoom: 50%;" />

-   可根据专业名称查询
-   可根据专业层次和专业类别筛选
-   可收藏某个专业
-   专业有
    -   简介
        -   介绍
        -   课程
        -   就业
        -   男女比
        -   关键词
    -   开设院校
    -   院校分数线

### 2.7. 高考圈

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060047303.png" alt="image-20231206004726266" style="zoom:50%;" />

#### 用户主页？



### 2.8. 我的

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060045919.png" alt="image-20231206004552884" style="zoom: 50%;" />

#### 2.8.1. 我的志愿表

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060048648.png" alt="image-20231206004848601" style="zoom:50%;" />

#### 2.8.2. 收藏

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312060049625.png" alt="image-20231206004912579" style="zoom:50%;" />

## 数据库设计

### 用户信息表

-   用户ID
-   用户昵称
-   用户账号
-   用户密码
-   wxid
-   用户身份（学生、家长、老师）
-   获赞数量
-   粉丝数量
-   关注数量
-   标签
-   IsDelete：0，1
-   AddTime

### 用户粉丝表

-   粉丝关系ID

-   用户ID
-   粉丝用户ID
-   关注时间
-   IsDelete：0，1
-   AddTime

### 用户关注表
-   关注关系ID
-   用户ID
-   被关注用户ID
-   关注时间
-   IsDelete：0，1
-   AddTime

### 高考信息表

-   高考信息表ID
-   用户ID
-   区域ID
-   批次类型ID
-   高年年份
-   选科组合：6位二进制表示，选中标1（六科分别为物化生史政地）
-   高考分数
-   高考排名
-   IsDelete：0，1
-   AddTime

### 院校录取概率表

-   院校录取概率表ID
-   高考信息表ID
-   大学ID
-   录取概率
-   类型（0-冲 1-稳 2 保）
-   IsDelete：0，1
-   AddTime

### 院校专业录取概率表

-   院校专业录取概率表ID
-   院校录取概率表ID
-   高考信息表ID
-   大学ID
-   专业ID
-   录取概率
-   类型（0-冲 1-稳 2 保）
-   IsDelete：0，1
-   AddTime

### 大学收藏表

-   大学收藏ID
-   用户ID
-   大学ID
-   收藏时间
-   IsDelete：0，1
-   AddTime

### 专业收藏表

-   专业收藏ID
-   用户ID
-   专业ID
-   收藏时间
-   IsDelete：0，1
-   AddTime

### 志愿表

-   志愿表ID
-   用户ID
-   志愿表名称
-   修改时间
-   高考信息表ID
-   IsDelete：0，1
-   AddTime

### 大学志愿表项

-   大学志愿表项ID
-   志愿表ID
-   大学ID
-   IsDelete：0，1
-   AddTime

### 专业志愿表项

-   专业志愿表项ID
-   大学志愿表项ID
-   专业ID
-   IsDelete：0，1
-   AddTime

### 大学排名表

-   大学ID
-   大学排名
-   排名分数
-   档次985
-   档次211
-   档次双一流
-   IsDelete：0，1
-   AddTime

### 大学位置表

-   大学ID
-   区域ID
-   IsDelete：0，1
-   AddTime

### 区域表

-   区域ID
-   区域名称
-   ParentID (父级区域ID)
-   Type：记录当前的区域级别：0--直辖市，1--省，2--市；3-地级市；4-区
-   IsDelete：0，1
-   AddTime

### 批次类型表

-   批次类型ID
-   批次名称
-   IsDelete：0，1
-   AddTime

### 区域批次表

-   区域批次表ID
-   区域ID
-   年份
-   批次类型ID
-   科目
-   批次分数
-   IsDelete：0，1
-   AddTime

### 大学录取分数线表

-   大学录取分数线表ID
-   大学ID
-   区域ID
-   年份
-   录取分数线
-   最低位次
-   IsDelete：0，1
-   AddTime

### 大学

-   大学ID
-   大学名称
-   院校层次
-   院校类型
-   地址
-   电话
-   官网
-   景色
-   IsDelete：0，1
-   AddTime

### 专业类型表

-   专业类型ID
-   专业类型名称
-   IsDelete：0，1
-   AddTime

### 专业大类表

-   专业大类ID
-   专业类型ID
-   专业大类名称
-   IsDelete：0，1
-   AddTime

### 专业

-   专业ID
-   专业大类ID
-   专业名称
-   专业简介
-   开设课程
-   就业方向
-   第一印象
-   IsDelete：0，1
-   AddTime

### 大学 _专业 _ 省份

-   大学 _专业 _ 省份 ID
-   大学ID
-   专业ID
-   区域ID
-   批次类型（0，1）
-   计划人数
-   分数线
-   最低位次
-   年份
-   限选科目：6位二进制表示，选中标1（六科分别为物化生史政地）；对于某一专业 不限选科6科全1，限选标1其他标0
-   IsDelete：0，1
-   AddTime

### 专业组表

-   专业组ID
-   专业组名称
-   学制
-   学费
-   招生计划
-   选课科目要求
-   IsDelete：0，1
-   AddTime

### 省份_专业组__专业表

-   ID
-   区域ID
-   专业组ID
-   专业ID
-   批次类型（0，1）
-   IsDelete：0，1
-   AddTime

### 一分一段表

-   一分一段ID

-   区域ID
-   年份
-   分数
-   人数
-   累计人数
-   IsDelete：0，1
-   AddTime

### 高考圈动态表

-   动态ID
-   用户ID
-   动态内容
-   点赞数量
-   回复数量
-   发布时间
-   区域ID
-   IsDelete：0，1
-   AddTime

Comment 表:

-   CommentID (评论ID):
    -   类型：主键
    -   说明：唯一标识每条评论和回复的编号。
-   Content (评论内容):
    -   类型：文本
    -   说明：评论或回复的具体内容。
-   Likes (点赞数量):
    -   类型：整数
    -   说明：评论或回复收到的点赞数量。
-   Replies (回复数量):
    -   类型：整数
    -   说明：评论或回复收到的回复数量。
-   Date (评论或回复时间):
    -   类型：日期时间
    -   说明：评论或回复的发表时间。
-   UserID (用户ID):
    -   类型：外键
    -   说明：与User表的UserID关联，表示发表评论或回复的用户。
-   ArticleID (高考圈动态ID):
    -   类型：外键
    -   说明：与Article表的ArticleID关联，表示评论或回复所属的文章。
-   区域ID
-   **ParentID (父评论ID):**
    -   类型：外键
    -   说明：与Comment表的CommentID关联，表示回复指向的评论。
-   IsDelete：0，1
-   AddTime

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312191208355.png" alt="image-20231219120857111" style="zoom:33%;" />

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312191209288.png" alt="image-20231219120909836" style="zoom:33%;" />

<img src="https://cdn.jsdelivr.net/gh/ZeirSor/picgo_img@main/202312191209364.png" alt="image-20231219120923720" style="zoom:33%;" />
