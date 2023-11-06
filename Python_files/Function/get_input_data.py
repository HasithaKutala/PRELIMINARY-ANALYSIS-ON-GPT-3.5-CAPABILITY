import pandas as pd
import psycopg2

class connectpostgre():
    def postgre_connection(self):
       
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="jira_dataset",
            user="postgres",
            password="Hasitha@3"
        )

        
        cursor = connection.cursor()
        
        
        cursor.execute("""
            SELECT DISTINCT 
                jira_issue_report.project_name,
                jira_issue_comment.comment,politeness,sentiment
            FROM 
                jira_issue_report 
            JOIN 
                jira_issue_comment 
            ON 
                jira_issue_report.id = jira_issue_comment.issue_report_id
            WHERE 
                jira_issue_report.project_name = 'ZooKeeper'
            
            Limit 5
            
            
        """)

      
        fetched_results = cursor.fetchall()

        df = pd.DataFrame(fetched_results, columns=['project_name', 'comments', 'politeness','sentiment'])
        
        
        


       
        connection.commit()
        cursor.close()

        connection.close()

        return df
