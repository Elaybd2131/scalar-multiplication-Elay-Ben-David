import numpy as np


def FindResult(arr, Filter):
    """
    מקבלת שני מערכים דו מימדיים
    מחזירה מערך עם תוצאות מכפלות סקלריות של הפילטר עם כל אחד משלשות המערך
    """
    result= np.zeros([arr.shape[0]-2, arr.shape[1]-2], dtype= float) # מערך עם תוצאות מכפלות סקלריות של הפילטר עם כל אחד משלשות המערך המתקבל
    for line in range (arr.shape[0] - 2): # ריצה על השורות
        for column in range (arr.shape[1] - 2): # ריצה על הטורים 
            c= arr[line :line + 3, column :column + 3]
            result[line, column]= Calc(c, Filter)
    return result


def Calc (c, Filter):
    """
    מקבלת את המערך הדו מימדי filter וחלק חתוך מן המערך arr בגודל 3 על 3
    הפעולה מחשבת ומחזירה תוצאה של מכפלה סקלרית בין שני המערכים
    """
    scalar= 0 # תוצאת המכפלה הסקלרית בין שני המערכים המתקבלים
    for x in range (3):
        lineC = c[x:x+1][0] # c שורה אחת מתוך המערך הדו מימדי
        lineF= Filter[x:x+1][0] # filter שורה אחת מתוך המערך הדו מימדי
        scalar= scalar + np.dot(lineC, lineF)
    return scalar


def main():
    arr= np.array([[1, 0, 1, 4, 3, 7, 3, 2], [1, 0, 1, 4, 3, 7, 3, 2], 
           [1, 0, 1, 4, 3, 7, 3, 2], [1, 0, 1, 4, 3, 7, 3, 2], 
           [1, 0, 1, 4, 3, 7, 3, 2], [1, 0, 1, 4, 3, 7, 3, 2],
           [1, 0, 1, 4, 3, 7, 3, 2] ,[1, 0, 1, 4, 3, 7, 3, 2]])
    Filter= np.random.rand(3, 3)
    #print ("arr: ", arr)
    #print ("Filter: ", Filter)
    while arr.shape[0] >= Filter.shape[0] and arr.shape[1] >= Filter.shape[1]:
        Filter= np.random.rand(3, 3)
        arr= FindResult(arr, Filter)
        print ("result: " , arr)



if __name__ == "__main__":
    main()    