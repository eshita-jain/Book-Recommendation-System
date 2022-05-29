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

![image](https://user-images.githubusercontent.com/80577092/170884625-f5701e5b-253d-43b3-b9fb-83bd4d319d9a.png)

REGISTER FOR SIGN-UP PAGE

![image](https://user-images.githubusercontent.com/80577092/170884658-1cdefa6f-e6fc-4db2-a4a0-71607ab387d8.png)


1. HOME PAGE

![image](https://user-images.githubusercontent.com/80577092/170884450-69970f31-921a-4457-83d9-afe96a4cf697.png)

![image](https://user-images.githubusercontent.com/80577092/170884466-c31d9508-a6be-4313-94c3-1dd50c9e39d7.png)

2. UPLOAD BOOK PAGE

![image](https://user-images.githubusercontent.com/80577092/170884488-aecf4b1e-8dbc-48b1-b5df-f1b607c607a7.png)

3. DELETE BOOK PAGE

![image](https://user-images.githubusercontent.com/80577092/170884509-e14535ff-3216-4723-b6c4-9065a9473d2f.png)

4. CONTACT US PAGE

![image](https://user-images.githubusercontent.com/80577092/170884535-a9fd26ec-229d-4d5d-a6bb-e7de3f7414ec.png)

5. RECOMMENDATION PAGE 

**Prominent part of our web-app:

![image](https://user-images.githubusercontent.com/80577092/170885791-46553692-5a83-4e01-ad0b-7530426d9668.png)

![image](https://user-images.githubusercontent.com/80577092/170885803-f20ff36b-0bf6-4710-8a90-edeeec347b72.png)



 
