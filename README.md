# Q3 螺旋矩陣 (20%)
給定一組數字，依照數字大小順序並以螺旋方式排成一個二維矩陣，這個矩陣就叫做螺旋矩陣。
例如:
給定數字1~9，依照大小順序並以逆時針方向螺旋方式排出方陣，結果如下

[[1, 8, 7], 
 [2, 9, 6], 
 [3, 4, 5]]

請根據上面的解釋，完成create_spiral_matrix函式，這個函式只有一個參數n，它決定了方陣的大小(n*n)與數值的最大值(n2)。
函式開頭的變數有matrix(初始化矩陣)、top(最上面的列的位置)、left(最左邊的行的位置)、bottom(最底下的列的位置)、right(最右邊的行的位置)、cnt(要填入矩陣的數值，每次有數值填入矩陣，cnt會累加1)，以上變數在編寫形成螺旋矩陣的部分都會被用到，請不要擅自更改。
這個函式需要回傳螺旋方陣，最後在主程式中輸入n的值並列出得到的螺旋方陣。
