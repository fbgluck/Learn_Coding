# files_read_from_CSV_file
<#
Read a CSV file of the form <lastName>,<firstName>,<graduaton_year><domain>
and create an email address of the form
<gradyear2digits><firstInitial><lastName>@sanford.org
e.g. 22fgluck@sanford.org
File sample: Gluck,Fredric,2022,wells.org
Write these to a file (and send a welcome email)
#>
# ref: https://www.howtogeek.com/120011/stupid-geek-tricks-how-to-send-email-from-the-command-line-in-windows-without-extra-software/
<# Test sending of email #>
<#
Send-MailMessage `
-To srtc@SRTCCNS.EDU `
-From srtc@SRTCCNS.EDU `
-SmtpServer 192.168.0.23 `
-Port 25 `
-Body "Hello There"
#>
# Note the full email address. The domain must appear in
# the mail server in the file /etc/mail/local-host-names
# this is the file that sendmail uses to check and see what
# domains it is allowed to deliver to.
$EmailFrom = “srtc@cns-ubuntu-server.srtccns.edu”
$EmailTo = “srtc@cns-ubuntu-server.srtccns.edu”
$Subject = “Test Subject”
$Body = “Hello Email”
$SMTPServer = “192.168.0.23”
$SMTPClient = New-Object Net.Mail.SMTPClient($SmtpServer, 25)
#$SMTPClient.EnableSsl = $true
#$SMTPClient.Credentials = New-Object System.Net.NetworkCredential(“usr”, “pass”);
$SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)