function output  = analysis ()
%% 读取数据
data = xlsread('niceDataAdjustedNoNoise.xlsx');
age = data(:,3);
income = data(:,4);
expenditure = data(:,5);
age5 = data(:,16);
LNincome = data(:,17);
oneThree = data(:,18);
threeTen = data(:,19);
minincome = min(income);
maxincome = max(income);
minage = min(age);
maxage = max(age);
%% 下面绘制图像
%scatter3(age, income, oneThree)

%% 下面绘制拟合的函数图像
% 年龄和收入数量级差别太大，首先做一定的坐标变换
X = linspace(10,80);
Y = linspace(10^4,10^7);
[x,y] = meshgrid(X,Y);
expenditure = -1.29*10^-4*x^5 + 0.8742*10^5*log(y)-7.733*10^5;
contourf(x,y,expenditure,'ShowText','on');
%xlabel('0.01*age^5');
%ylabel('1*10^5*ln(income)');

X = linspace(10,80);
Y = linspace(10^4,10^7);
[x,y] = meshgrid(X,Y);
oneThree = 0.0028*x + 1.077*10^(-9)*y+0.1878;

contourf(x,y,oneThree,'ShowText','on');

X = linspace(10,80);
Y = linspace(10^4,10^7);
[x,y] = meshgrid(X,Y);
threeTen = 0.0065*x + 2.346*10^-9*y-0.0172;
contourf(x,y,threeTen,'ShowText','on');
