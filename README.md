# Book-Recommendation-System

![buch](https://user-images.githubusercontent.com/80577092/170884683-22ae4009-6efd-4cc2-afcf-055ed43a802c.png)


Good Old Friend - A book Recomemder for all the book lovers out their .To save thier time and easily provide them their Favorite books based on the genre they prefer to read, most liked content and the books that are highly rated by the users.

Good old friend is a simple yet powerfull web app made using flask framework to recommed your favourate book using content based filtering and cosine similarity metrices.

Front-end : Developed using HTML and CSS.

Back-end : Flask Framework.

How to run ?

Steps:

1. Clone the repositary in your local device.
2. Install all the requirements using :

`pip install -r requirements.txt`

3. Then extract the bookdataset.zip in your directory 
 Then change the path of dataset in the recomm.py file in line number 13 and 16.

4. Now simply run the server in terminal using
  
`python run.py`

# ALGORITHMS USED

* CONTENT BASED FILTERING:
Content based recommender systems take into account the data provided by the user both directly or indirectly. For example, age can be used to determine classes of products or items reviewed or bought by the user. This type of recommender system relies on characteristics of object. New content can be quickly recommended to the user. These type of systems does not take into account behavior/ data about other users in the systems but here things are little changed.

* COSINE SIMILARITY:
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

Similarity Score :

How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

# GLIMPSE OF THE WEB-APP

MY ACCOUNT PAGE 

![image](https://github.com/user-attachments/assets/fc125070-6193-41b9-963e-8fc84edab559)

REGISTER FOR SIGN-UP PAGE

![image](https://github.com/user-attachments/assets/cc7a4676-739d-4e0f-9ecb-66e76a6ee5ea)


1. HOME PAGE

![image](https://github.com/user-attachments/assets/1bf86b20-dd00-438e-9f60-7de07f0aa9f9)


![image](https://github.com/user-attachments/assets/fc74dbfb-7278-4ecb-8327-64aac634b624)


2. UPLOAD BOOK PAGE

![image](https://github.com/user-attachments/assets/5e8f3332-ec85-46bf-aa89-a2f8ac0ab46e)

3. DELETE BOOK PAGE

![image](https://github.com/user-attachments/assets/f163f948-e633-4e19-b0af-6ffc9356e1d6)

4. CONTACT US PAGE

![image](https://github.com/user-attachments/assets/b658a21d-df50-4e9b-9d4b-0b972476bb9c)


5. RECOMMENDATION PAGE 

**Prominent part of our web-app:

![image](https://github.com/user-attachments/assets/c3ca3aba-500e-4743-97fb-225682df1b58)

![image](https://github.com/user-attachments/assets/9d1e6dd9-4308-49dd-9803-35f3682edf6d)




 
