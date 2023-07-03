import pandas as pd
import socket

host = '192.168.5.107'  # Replace with the actual remote host
port = 5000  # Replace with the actual port number

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

jar_filename = 'feed-play-1.0'  # Replace with the actual JAR file name
sock.sendall(jar_filename.encode())

# Create an empty DataFrame to store the data
df = pd.DataFrame(columns=['Symbol', 'LTP', 'LTQ' , 'TotalTradedVolume','BestBid','BestAsk','BestBidQty','BestAskQty','OpenInterest','Timestamp','PrevClosePrice','PrevOpenInterest'])  # Adjust column names as needed

while True:
    data = sock.recv(9011).decode()
    if not data:
        break
    
    # Process the received data and append it to the DataFrame
    # Assuming the data is in the format "value1,value2,value3"
    row = data.strip().split(',')
    df.loc[len(df)] = row

# Close the socket connection
sock.close()

# Print or use the DataFrame as needed
print(df)
