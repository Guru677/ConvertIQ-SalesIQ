Problem Statement:

"ConvertIQ is an AI-powered SalesIQ chatbot that predicts website visitor drop-off risk in real time using behavioural patterns and sentiment analysis. When the bot detects a visitor who is likely to leave, it proactively engages the visitor and alerts human operators to reduce churn and increase conversions."

















🔷 ConvertIQ System Architecture (Easy Explanation)

1️⃣ Visitor enters website



\-Opens the demo website

\-Starts browsing pages

\-SalesIQ automatically tracks behaviour



2️⃣ SalesIQ bot collects behaviour data



\-Bot captures:

\-time on page

\-idle time

\-scroll depth

\-message sentiment

\-clicks

\-pages visited



3️⃣ Bot sends this data to ConvertIQ AI Model



Bot → sends JSON → to your FastAPI/Flask ML server.



Example:



{

&nbsp; "time\_on\_page": 20,

&nbsp; "sentiment\_score": -1,

&nbsp; "pages\_visited": 3

}



4️⃣ ML Model predicts drop-off risk



AI Model returns:



{

&nbsp; "risk": "High",

&nbsp; "confidence": 0.82

}



5️⃣ Bot decides the action based on risk



-High → notify human operator + send proactive help

-Medium → send helpful suggestions

-Low → continue normal chat



6️⃣ Operator receives real-time alerts



Notifications show:



"⚠️ Visitor #123 may drop off. Engage now."



Helps team take action faster.



7️⃣ Analytics widget displays visitor risk levels



-You may build a simple dashboard:

-Number of high-risk visitors

-Average sentiment

-Drop-off likelihood over time

