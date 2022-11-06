git init
git commit -m "Initial project setup"
git branch -M main
git add *
git commit -m "Initial project setup"
git branch -M main
git remote add origin https://github.com/cherotich/company_social_media_feed.git
git push -u origin main
kedro pipeline create data_collection
kedro pipeline create data_analytics
kedro pipeline create data_processing
kedro docker run
kedro docker run
