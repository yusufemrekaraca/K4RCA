$url = 'https://www.infobyip.com/'; 
$wr = Invoke-WebRequest -UseBasicParsing $url; 
$wr.RawContent | out-file -FilePath ip.html -Force
