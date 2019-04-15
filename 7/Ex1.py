#Решить с помощью генераторов списка.
#
#1. Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

#    Примечание: Списки фруктов создайте вручную в начале файла.


firstList=['Apple','Orange', "Watermelon", "Pineapple"]
secondList=["Berberry", "Cherry", "Apple", "Strawberry", "Pineapple"]

crossList=[]

crossList=[fruit for fruit in firstList if fruit in secondList]

print (crossList)