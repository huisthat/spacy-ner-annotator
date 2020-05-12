import spacy
import random

# with open('training_data.txt', 'r', encoding='utf-8') as f:
#     training_data = f.readlines()

# training = training_data[0]
# print(training)
TRAIN_DATA = [('Spam messages by Zeus might contain a neutral text that looks as though it was sent from an acquaintance, such as “Hi! How was the weekend trip? I have some news for you! Check this out, you won’t believe it: http://rss.lenta-news.ru/subj/vesti.exe”. ', {'entities': [(244, 248, 'File Type')]}), ('These Zeus emails contained a ZIP archive that contained a JavaScript file.', {'entities': [(30, 33, 'File Type')]}), ('Emails often appear to be sent from legitimate sources — Starbucks inviting you to a special event, Facebook or LinkedIn asking you to log in to accept a friend request, or your bank claiming someone has made a payment in your name, and inviting you to download an executable file to cancel it.', {'entities': [(265, 280, 'File Type')]}), ('Many of them next downloaded a Windows PE executable file (which will be detected by Talos Certified SID 11192); typically, these binaries are updates to the Zeus client software, to ensure that the newly infected host is up-to-date in its capabilities.', {'entities': [(31, 57, 'File Type')]}), ('A recently spotted spam campaign was using Message (.MSG) file attachments to infect users with the infamous Zbot banking Trojan, Trustwave security researchers say.', {'entities': [(43, 50, 'File Type'), (52, 56, 'File Type')]}), ('The spam run contained alleged Tax Notification emails coming from Canada Revenue Agency, which had the aforementioned MSG file attached.', {'entities': [(119, 122, 'File Type')]}), ('What Trustwave researchers focused on was the extraction of the malicious Zeus object from the .MSG file without using Outlook, and they started by confirming that the file was an OLE (Object Linking and Embedding) compound file – used for storing MS Office documents. ', {'entities': [(95, 99, 'File Type'), (180, 183, 'File Type'), (185, 213, 'File Type')]}), ('When run, the JavaScript would download a malicious executable from the domain “tradestlo[.]top,” which researchers say was a Trojan downloader called Terdot. ', {'entities': [(14, 24, 'File Type'), (52, 62, 'File Type')]}), ("The Zeus variants in the campaign we're about to describe also appear to be using Zeus droppers that employ the hidden Windows 'PIF' file extension - a file extension that used to be popular many years back, that was often associated with viruses then, and that appears to be making a comeback.", {'entities': [(128, 131, 'File Type')]}), ("In this case, the bot can update itself by downloading an executable file using SSL, which will defeat any sandbox that doesn't employ SSL inspection. For example: hxxps://invoice-maker.ru/flash/flashplayer.exe.", {'entities': [(58, 68, 'File Type'), (206, 210, 'File Type')]}), ('The attack tried to entice victims to open a ZIP attachment containing the Upatre downloader on their computer, which would later infect the users with Zeus GameOver.', {'entities': [(45, 48, 'File Type')]}), ('This campaign combines an HTML or ZIP attachment with a social engineering technique, similar to what we normally see in malicious email campaigns. ', {'entities': [(26, 30, 'File Type'), (34, 37, 'File Type')]}), ('Opening the attachment results in a compromised user machine via an obfuscated JavaScript in the attached HTML file.', {'entities': [(79, 89, 'File Type'), (106, 110, 'File Type')]}), ('The Zeus Panda sample used automated transfer scripts (ATS) to inject code into banking websites. ATS are essentially javascript files which are hosted on a third party website, and contain code which will change the content of a banking website. ', {'entities': [(27, 53, 'File Type'), (55, 58, 'File Type')]}), ('This new variant uses a malicious PDF file which contains the threat as an embedded file. When recipients open the PDF, it asks to save a PDF file called Royal_Mail_Delivery_Notice.pdf. ', {'entities': [(180, 184, 'File Type'), (34, 37, 'File Type')]}), ('The messages carried a zip attachment containing an executable that is a variant of the Trojan.Zbot.', {'entities': [(23, 26, 'File Type'), (52, 62, 'File Type')]}), ('The Zeus e-mails contain an MSG attachment with an embedded OLE object. This is not a technique we see very often and is challenging for security products to detect due to the complicated MSG format.', {'entities': [(28, 31, 'File Type')]}), ('The latest Gameover variant is being distributed through spam emails purporting to come from HSBC France with fake invoices in .zip attachments.', {'entities': [(127, 132, 'File Type')]}), ('At the beginning of February, researchers from security firm Malcovery Security, reported that a new variant of Zeus Gameover was being distributed as an encrypted .enc file in order to bypass network-level defenses. ', {'entities': [(164, 168, 'File Type')]}), ('As Zeus is primarily email based, it would be prudent to block email attachments containing executable files or ZIP files with file extensions like EXE or SCR or ZIP (but not limited to these).', {'entities': [(148, 151, 'File Type'), (92, 102, 'File Type'), (112, 115, 'File Type'), (155, 158, 'File Type')]}), ('Like similar malware campaigns, Terdot attacks begin with phishing emails. These messages are rigged with a button designed to look like a PDF file, which when clicked will actually execute Javascript code to download the malware file.', {'entities': [(190, 200, 'File Type'), (139, 142, 'File Type')]}), ('Once the initial component of Zloader runs, it deploys Windows Explorer (explorer.exe) and injects shellcode along with a new Portable Executable (PE) file containing payload.dll.', {'entities': [(81, 85, 'File Type'), (126, 145, 'File Type')]}), ("The trojan Zeus is sending out email on port 25 from the workstation that's infected.", {'entities': [(40, 47, 'Port')]}), ('This anomality was detected by a TCP/IP connection from <our external IP> on port 1992 going to an the sinkhole on port 80, which was by Zbot', {'entities': [(115, 122, 'Port'), (77, 86, 'Port')]}), ('For POP3 data (port 110), the hook procedure records the user names and passwords of USER and PASS commands, and also examines buffers that are at least 12 characters in length for an initial AUTH PLAIN command. ', {'entities': [(15, 23, 'Port')]}), ('For HTTP data (port 80), the hook procedure searches the entire sent buffer for the string \\r\\nAuthorization: Basic and, if found, extracts the data that follows, stopping at the next \\r\\n sequence or at the end of the buffer and then submitting the base-64-decoded data to the zbot server.', {'entities': [(15, 22, 'Port')]}), ('The Zeus malware tells the browser to run traffic through TCP port 9050 and the stolen data will eventually land in an onion domain.', {'entities': [(62, 71, 'Port')]}), ('An example behavioral pattern that we can analyze are all the flows sent by the zbot to the destination port 8033 using the UDP protocol. ', {'entities': [(104, 113, 'Port')]}), ('We also noted that the zbot started a server listening on ports 1548 and 3492. ', {'entities': [(58, 68, 'Port'), (73, 77, 'Port')]}), ('When the malware successfully contacts a live C2 server, the Zeus malware sends RSA-encrypted data using a request on TCP port 80 (see Figure 2).', {'entities': [(122, 129, 'Port')]}), ('After terdot sent queries, it is followed by connections to that host via TCP port 443 ', {'entities': [(78, 86, 'Port')]}), ('The Tor utility maintained by Zeus under the cover of the svchost.exe process creates an HTTP proxy server listening to the TCP port 9050.', {'entities': [(128, 137, 'Port')]}), ('They reach your machine where tor.exe maintained by Zeus accepts a connection on port 80 and redirects it to port 1080 on the local machine which is listened to by the web server.', {'entities': [(81, 88, 'Port'), (109, 118, 'Port'), (33, 37, 'File Type')]}), ('Zeus was listening on TCP port 9050 that is the Tor port, there were some active network Tor connections and Opera was causing a massive flooding of TCP connections.', {'entities': [(26, 35, 'Port')]}), ("Zeus uses port 80(HTTP) for all its communication between the victim's system and the C2 server.", {'entities': [(9, 17, 'Port')]}), ('In order to view the contents, the web browser (in this case, Firefox) connects to localhost on port 2222 (entry 2 and 3). The connection is received by the explorer.exe process (because it is where ZeuS injected its worker threads).', {'entities': [(96, 105, 'Port'), (165, 169, 'File Type')]}), ('Zeus listens on TCP port 80 for incoming connections and simply relays data receives to another server that hosts the actual phishing pages and malware files.', {'entities': [(20, 27, 'Port')]}), ('Our machine infected by Zeus was making connections with an ipv4 by the 80/tcp port. ', {'entities': [(72, 83, 'Port')]}), ('After monitoring and stealing data, the Zeus PIF variants communicate with C&C servers using HTTPS in order to transfer stolen data. ', {'entities': [(45, 48, 'File Type')]}), ('We observe that explorer.exe (Terdot malware)is communicating with an external server over HTTP.', {'entities': [(24, 28, 'File Type')]}), ('It uses two ways to Steal the data.one is by inspecting the client request or injecting the javascript spyware code, the second one is collecting logs from relevant data in HTTP requests and uploads them periodically to the C&C servers.', {'entities': [(92, 102, 'File Type')]}), ('Zeus creates the following registry entry to ensure persistence upon system reboot: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ Epoxs = "%Local Settings%\\Temp\\Eqxav\\epoxs.exe"', {'entities': [(178, 182, 'File Type')]}), ('Next, the Zeus malware creates a run key in the Registry under HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ with the path to the DLL set under %APPDATA% as a persistence method using Rundll32.exe and DllRegisterServer as an argument.', {'entities': [(198, 202, 'File Type')]}), ('The Zeus malware appends the path C:/Windows/System32/sdra64.exe to HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/WindowsNT/CurrentVersion/Winlogon/Userinit registry key.', {'entities': [(60, 64, 'File Type')]}), ('The emails used by Zeus PIF often hold subjects used to lure a target to run a file from a URL and according to the team are of good quality; containing no spelling mistakes and convincing imagery. ', {'entities': [(24, 27, 'File Type')]}), ('The email does not contain attachments, but rather a URL link to a .ZIP file which contains the Zeus dropper and the executable PIF file.', {'entities': [(67, 71, 'File Type'), (117, 132, 'File Type')]}), ('If execution is allowed then the JScript file will begin to download and execute Zeus malware from the following URL: hxxp://tradestlo.top/poll.hls', {'entities': [(33, 40, 'File Type')]}), ("The email messages don't contain file attachments, but rather a URL link to a ZIP file that contains a PIF file that is the Trojan Zeus Dropper. PIF is another executable extension (like .exe, etc.) and it operates like other executable files.", {'entities': [(78, 81, 'File Type'), (187, 191, 'File Type'), (103, 106, 'File Type')]}), ('If execution is allowed then the JScript file will begin to download and execute malware from the following URL: hxxp://tradestlo.top/poll.hls', {'entities': [(33, 40, 'File Type')]}), ('Opening the attached ZIP archive reveals a malicious file named "E-statement.pdf.scr" (MD5: 5e5e46145409fb4a5c8a004217eef836) that displays a familiar Adobe Reader PDF icon. ', {'entities': [(21, 24, 'File Type'), (80, 84, 'File Type')]}), ('There are two links in the message that lead to the same IP address hosting a PDF file for instructions and an executable that is meant to be the patch to apply. The executable file named adbp932b.exe (SHA1 0632f562c6c89903b56da235af237dc4b72efeb3) has minimal coverage of about 7%.', {'entities': [(78, 81, 'File Type'), (196, 200, 'File Type'), (111, 121, 'File Type')]}), ('The Zeus Panda sample we analysed (SHA1 ccf17e27c0e5883920bb6abea5bc5d6c2c7a1c37) used automated transfer scripts (ATS) to inject code into banking websites. ', {'entities': [(87, 113, 'File Type'), (115, 118, 'File Type')]}), ('The attacks associated with the new botnet attempted to exploit the CVE-2017-17215 zero-day vulnerability in the Huawei home router caused by the fact that the TR-064 technical report standard, which was designed for local network configuration, was exposed to WAN through port 37215 (UPnP – Universal Plug and Play).', {'entities': [(273, 283, 'Port')]}), ('About 12 hours ago (2017-12-05 11:57 AM GMT+8), we noticed a new version of Satori (a mirai variant which we named Satori), starting to propagate very quickly on port 37215 and 52869.', {'entities': [(162, 172, 'Port'), (177, 182, 'Port')]}), ('Two new exploits, which work on port 37215 and 52869 have been added, see below for more details.', {'entities': [(32, 42, 'Port'), (47, 52, 'Port')]}), ('Due to the worm like behavior, we all should be on the lookout for the port 37215 and 52869 scan traffic.', {'entities': [(71, 81, 'Port'), (86, 91, 'Port')]}), ('For those who don’t have the visibility, feel free to check out our free Scanmon system for port 37215 and 52869, or ISC port pages for 37215 and 52869.', {'entities': [(97, 102, 'Port'), (107, 112, 'Port')]}), ('As can be seen from the following picture, the bot will scan port 37215 and 52869 randomly, determined by the remainder of a random integer mod 3.', {'entities': [(61, 71, 'Port'), (76, 81, 'Port')]}), ('During the scanning, Satori will utilize two different exploits, one on port 37215, while the other on 52869.', {'entities': [(72, 82, 'Port'), (103, 108, 'Port')]}), ('The one on port 37215 is not fully disclosed yet, our team has been tracking this in the last few days and got quite some insight, but we will not discuss it here right now.(stay tuned for our update later).', {'entities': [(11, 21, 'Port')]}), ('For example, during last recent 12 hours we have seen 263,250 different IPs scanning port 37215, and 19,403 IPs scanning port 52869.', {'entities': [(85, 95, 'Port'), (121, 131, 'Port')]}), ('The scanner process runs continuously on each mirai BOT using the telnet protocol (on TCP port 23 or 2323) to try and login to IP addresses at random. ', {'entities': [(90, 97, 'Port'), (101, 105, 'Port')]}), ('To infect these devices Mirai chooses random IPs and attempts to use default administrative credentials to take over the device via ports 7547 and 5555 ', {'entities': [(132, 142, 'Port'), (147, 151, 'Port')]}), ('These ports are: port 53413 related to Netis Routers, port 37215 related to Huawei HG532 routers, port 52869 UPnP SOAP service from a Realtek SDK, and port 81 for CCTV-DVR cameras. ', {'entities': [(16, 28, 'Port'), (54, 64, 'Port'), (98, 108, 'Port'), (150, 158, 'Port')]}), ('In the subsequent seven consecutive days, the system received the same attack payload sent from multiple infected IP addresses. The attack targeted TCP port 5555. ', {'entities': [(152, 161, 'Port')]}), ('ADB.Mirai spreads via the ADB port of Android devices, and this sample randomly generates 359 IP addresses and scans port 5555 on these addresses to seek for exploitable targets. ', {'entities': [(117, 126, 'Port')]}), ('ADB.Mirai spreads via the ADB port of Android devices. This sample randomly generates 359 IP addresses and scans port 5555 on these addresses to seek for exploitable targets. ', {'entities': [(113, 122, 'Port')]}), ('Affected routers use protocols that leave port 7547 open, which allows for exploitation of the router. ', {'entities': [(42, 51, 'Port')]}), ('Monitor Internet Protocol (IP) port 2323/TCP and port 23/TCP for attempts to gain unauthorized control over IoT devices using the network terminal (Telnet) protocol by Mirai', {'entities': [(31, 38, 'Port')]}), ('Mirai spread by first entering a quick scanning stage where it proliferates by haphazardly sending TCP SYN probes to pseudo-random IPv4 addresses, on Telnet TCP ports 23 and 2323.', {'entities': [(160, 169, 'Port'), (174, 178, 'Port')]}), ('So as to strengthen itself, Mirai also terminates different services which are bound to TCP/22 or TCP/23, including other Mirai variations. ', {'entities': [(88, 94, 'Port'), (98, 104, 'Port')]}), ('The destination port numbers of scanning packets are distributed as ∼90% port 23 and ∼10% port 2323 for Mirai.', {'entities': [(73, 80, 'Port'), (90, 99, 'Port')]}), ('Satori, the new variant of Mirai is different from all previous variants as it does not use a Telnet port scanner instead it will scan TCP ports 37215 and 52869 on random IP addresses. ', {'entities': [(139, 150, 'Port'), (155, 160, 'Port')]}), ('The Satori attack is employed with two new exploits which is targeting TCP ports 37215 and 52869.', {'entities': [(75, 86, 'Port'), (91, 96, 'Port')]}), ('One of the exploit by Satori works on TCP port 52869 of IoT devices/routers.', {'entities': [(42, 52, 'Port')]}), ("The bug leaves the router's TCP port 7547 exposed to the internet.", {'entities': [(32, 41, 'Port')]}), ('ISPs should restrict access to ports 7547 (and 5555) accordingly in order to protect routers from exploits against unpatched vulnerabilities by Mirai.', {'entities': [(31, 41, 'Port'), (47, 51, 'Port')]}), ('When a router is infected by the new Mirai variant it closes port 7547 and disables telnet as well, making it very difficult for ISPs to apply patches remotely.', {'entities': [(61, 70, 'Port')]}), ('We see that on September 13, 2016, port 2323 (TCP), an alternate port for Telnet, began showing up in our top five most-scanned ports. Port 23 (TCP), the standard port for Telnet, often shows up in the top five. Both ports are associated with the Mirai botnet, which scans them looking for vulnerable IoT devices.', {'entities': [(35, 44, 'Port'), (135, 143, 'Port')]}), ('The Mirai code was modified to include exploitation of another vulnerability, TR-06927, and used TCP port 7547.', {'entities': [(101, 110, 'Port')]}), ('At the end of January 2017 our port metrics still showed significant scans for port 23 (Telnet), and while activity on ports 2323 and 7547 was still occurring, the volume was lower.', {'entities': [(79, 86, 'Port'), (119, 129, 'Port'), (134, 138, 'Port')]}), ('Mukashi searches open TCP port 23 and uses combinations of default credentials to access other systems. The bot supports various commands, like Mirai, such as launching DDoS attacks.', {'entities': [(26, 33, 'Port')]}), ('Mukashi binds to the TCP port 23448 in order to ensure only a single instance is running on the infected system.', {'entities': [(25, 35, 'Port')]}), ('Wicked, a Mirai variant, scans ports 8080, 8443, 80 and 81 by initiating a raw socket SYN connection; if a connection is established, it will attempt to exploit the device and download its payload.', {'entities': [ (43, 47, 'Port'), (37, 39, 'Port'), (56, 58, 'Port')]}), ('The C2 servers for Emotet can receive these communications on port 80, which is the default port for HTTP, but may also receive them on port 443, which is the default for HTTPS traffic, or on a number of other nonstandard ports, including but not limited to 7080, 8080, 8090, 50000, or several others.', {'entities': [(61, 69, 'Port'), (136, 144, 'Port'), (258, 262, 'Port'), (264, 268, 'Port'), (270, 274, 'Port'), (276, 281, 'Port')]}), ('After initial installation, the C2 capabilities begin. Emotet connects to C2 servers on various ports including, but not limited to: 20, 80, 443, 7080, 8443, and 50000.', {'entities': [(133, 135, 'Port'), (137, 139, 'Port'), (141, 144, 'Port'), (146, 150, 'Port'), (152, 156, 'Port'), (162, 167, 'Port')]}), ('The above example for Emotet demonstrates HTTP running on port 20 to one of those hard-coded IP addresses. ', {'entities': [(58, 65, 'Port')]}), ('If the connection is successful, Emotet sleeps for 14 seconds before sending an HTTP POST to its Command and Control (C2) server on port 8080.', {'entities': [(132, 141, 'Port')]}), ('Although the Emotet connection to the server uses port 443, which is normally used for Transport Layer Security (TLS) encrypted communications, the connection is unencrypted HTTP. ', {'entities': [(50, 58, 'Port')]}), ('Emotet has used ports 20, 22, 80, 443, 8080, and 8443.', {'entities': [(16, 24, 'Port'), (26, 28, 'Port'), (30, 32, 'Port'), (34, 37, 'Port'), (39, 43, 'Port'), (49, 53, 'Port')]}), ('In some of the controller IPs, we observed HTTP traffic being sent over port 443.', {'entities': [(72, 80, 'Port')]}), ('The initial executable by Emotet appears to launch an application application lpiograd.exe, seen in Figure 2 and then looks to make outbound network connections on port 80, to a single command and control (CnC) server.', {'entities': [(164, 171, 'Port'), (86, 90, 'File Type')]}), ('Based on our visibility over the last 30 days, 14 Emotet IPs communicated with 5.45.65[.]126 on port 80/TCP.', {'entities': [(96, 103, 'Port')]}), ('Traffic observed to 212.8.242[.]201 was similar, with 23 Emotet IPs communicating on port 80/TCP. ', {'entities': [(85, 92, 'Port')]}), ('Once installed, the Emotet connects with the C2 server of hackers using specific ports that include 20, 80, 443, 7080, 8443, and 50000.', {'entities': [(100, 102, 'Port'), (104, 106, 'Port'), (108, 111, 'Port'), (113, 117, 'Port'), (119, 123, 'Port'), (129, 134, 'Port')]}), ('After gaining the persistency and enumerating the compromised host the next stage of Emotet is to connect to a new IP address on port 80.', {'entities': [(129, 136, 'Port')]}), ('On port 80 Emotet is running a standard Plesk HTTPd, which suggests the server is again a web server, but this time it doesn’t appear to be running any websites. ', {'entities': [(3, 10, 'Port')]}), ('In the Emotet config the port specified is 8080.', {'entities': [(43, 47, 'Port')]}), ('The port used by the Emotet loader is hardcoded into it – 8080.', {'entities': [(58, 62, 'Port')]}), ('Emotet has used ports 20, 22, 80, 443, 8080, and 8443.', {'entities': [(22, 24, 'Port'), (26, 28, 'Port'), (30, 32, 'Port'), (34, 37, 'Port'), (39, 43, 'Port'), (49, 53, 'Port')]}), ('The dissection of this suspicious file, known by Symantec as Trojan.Emotet, shows common elements such as: TCP communication over ports 80, 8080.', {'entities': [(136, 138, 'Port'), (140, 144, 'Port')]}), ('Emotet connects to C2 servers on various ports including, but not limited to: 20, 80, 443, 7080, 8443, and 50000', {'entities': [(78, 80, 'Port'), (82, 84, 'Port'), (86, 89, 'Port'), (91, 95, 'Port'), (97, 101, 'Port'), (107, 112, 'Port')]}), ('We can see that port 80 returns the same universal 404 error as the hacked server did on the Emotet port, so most likely this is the port it forwards traffic to.', {'entities': [(16, 23, 'Port')]}), ('The C2 servers can receive these communications on port 80, which is the default port for HTTP, but may also receive them on port 443, which is the default for HTTPS traffic, or on a number of other nonstandard ports, including but not limited to 7080, 8080, 8090, 50000, or several others. ', {'entities': [(51, 58, 'Port'), (124, 133, 'Port'), (247, 251, 'Port'), (253, 257, 'Port'), (259, 263, 'Port'), (265, 270, 'Port')]}), ('The initial executable appears to launch an application application lpiograd.exe, seen in Figure 2 and then looks to make outbound network connections on port 80, to a single command and control (CnC) server', {'entities': [(76, 80, 'File Type'), (154, 161, 'Port')]}), ('Emotet Trojan used commonly used port for communication (e.g TCP port 80, 8080, 443, 8443, 7080, 20, 22, 53)', {'entities': [(65, 72, 'Port'), (74, 78, 'Port'), (80, 83, 'Port'), (85, 89, 'Port'), (91, 95, 'Port'), (97, 99, 'Port'), (101, 103, 'Port'), (105, 107, 'Port')]}), ('***5.101.138.188 port 80 - sloegincottage.co.uk - GET /tyoinvur/En_us/Clients/092018/', {'entities': [(17, 24, 'Port')]}), ('***108.167.161.63 port 80 - louisianaplating.com - GET /18Ge0wDF', {'entities': [(18, 25, 'Port')]}), ('***50.62.194.30 port 80 - c-t.com.au - GET /PspAMbuSd2', {'entities': [(16, 24, 'Port')]}), ('***37.120.175.15 port 80 - Attempted TCP connections, no response from the server', {'entities': [(17, 24, 'Port')]}), ('Based on our visibility over the last 30 days, 14 IPs communicated on port 80/TCP, 13 of which were validated Tier 1 C2s. ', {'entities': [(70, 77, 'Port')]}), ('Traffic observed to 212.8.242[.]201 was similar, with 23 IPs communicating on port 80/TCP, 22 of which were validated Tier 1 C2s.', {'entities': [(77, 85, 'Port')]}), ('One technique is by simply swapping a .doc file with a .docx, which can make static detection of maldocs more difficult due to the compression native in the .docx format. ', {'entities': [(38, 42, 'File Type'), (55, 60, 'File Type')]}), ('While the attached documents all have a .doc extension, they are in fact .dotm, .docx, and other document file types, which enables them to successfully hide the embedded objects as ActiveX objects rather than typical “Form” objects whose metadata can be easily accessed in an opened document.', {'entities': [(40, 44, 'File Type'), (73, 78, 'File Type'), (80, 85, 'File Type')]}), ('However, the document in this case is not the usual .doc or .docx but rather an XML file masquerading as a .doc, and the macro in this instance makes use of the Shapes feature,', {'entities': [(80, 83, 'File Type'), (60, 65, 'File Type'), (51, 56, 'File Type')]}), ('Cybercriminals are attaching .pdf, .mp4, and .docx files to emails that purport to have information on how people can protect themselves from the virus, updates on its spread and even virus detection procedures. ', {'entities': [(29, 33, 'File Type'), (35, 39, 'File Type'), (45, 50, 'File Type')]}), ('The Emotet malware will disguise itself as a website hyperlink or regular file attachment in an email (.doc, .docx, .PDF), that will include hidden code that enables cybercriminals to gain control of your computer and other devices, often leading to the deployment of ransomware.', {'entities': [(103, 107, 'File Type'), (109, 114, 'File Type'), (116, 120, 'File Type')]}), ('Known as Emotet, the trojan is attached under the guise of pdf, mp4 and docx files.', {'entities': [(59, 62, 'File Type'), (64, 67, 'File Type'), (72, 76, 'File Type')]}), ('Emotet is most commonly spread via malicious emails containing Microsoft Office attachments, usually Microsoft Word (.doc, .docx) documents.', {'entities': [(117, 121, 'File Type'), (122, 128, 'File Type')]}), ('Microsoft will also force a different file extension (.docm instead of .docx for new documents containing macros).', {'entities': [(54, 59, 'File Type'), (70, 76, 'File Type')]}), ('It is most commonly spread via Microsoft Office attachments, usually Microsoft Word (.doc, .docx) documents.', {'entities': [(85, 89, 'File Type'), (90, 96, 'File Type')]}), ('Also, security experts at Kaspersky identified this malware spreading in form of pdf, mp4 and Docx files.', {'entities': [(81, 84, 'File Type'), (86, 89, 'File Type'), (94, 98, 'File Type')]}), ('According to security firm Kaspersky, attackers are using several types of malicious files, including pdf, mp4 and docx with “coronavirus” theme to spread malware.', {'entities': [(102, 105, 'File Type'), (107, 110, 'File Type'), (115, 119, 'File Type')]}), ('The archive contains an exe-file with a long name (to hide the extension) and a PDF document icon.', {'entities': [(24, 27, 'File Type'), (80, 83, 'File Type')]}), ('Once clicked on, the link will download a malicious pdf file containing the trojan.', {'entities': [(52, 55, 'File Type')]}), ('Emotet disguises itself as different pdf files in email attachments to bait users into clicking it.', {'entities': [(37, 40, 'File Type')]}), ('Such emails usually lead unsuspecting users to download the file attachments that can come in the form of .pdf, .mp4, and .docx. ', {'entities': [(106, 110, 'File Type'), (112, 116, 'File Type'), (122, 127, 'File Type')]}), ('Cylance has seen PDFs, XML Documents, and .js files all used in malicious Emotet spam.', {'entities': [(17, 21, 'File Type'), (23, 26, 'File Type'), (42, 45, 'File Type')]}), ('Contained within the body of one of the Emotet emails is a zip file attachment that contains an infected Word document (SHA-256: c58f07f84d6aae485416683e5515b39bc39349e69bc14629440e693da23d6c4d) with a malicious macro that calls PowerShell. ', {'entities': [(59, 62, 'File Type'), (105, 109, 'File Type')]}), ('In this blog, all analysis is based on the payload p4xl0bbb85.exe (sha256:21145645cac74e0b590813eafd257a2c4af6c6be0bc86d873ad0e6c005c0911d).', {'entities': [(61, 66, 'File Type')]}), ('The attacks associated with the new botnet attempted to exploit the CVE-2017-17215 zero-day vulnerability in the Huawei home router caused by the fact that the TR-064 technical report standard, which was designed for local network configuration, was exposed to WAN through port 37215 (UPnP – Universal Plug and Play).', {'entities': [(68, 82, 'SV')]}), ('About 12 hours ago (2017-12-05 11:57 AM GMT+8), we noticed a new version of Satori (a mirai variant which we named Satori), starting to propagate very quickly on port 37215 and 52869.', {'entities': [(162, 182, 'Port')]}), ('Two new exploits, which work on port 37215 and 52869 have been added, see below for more details.', {'entities': [(32, 52, 'Port')]}), ('Due to the worm like behavior, we all should be on the lookout for the port 37215 and 52869 scan traffic.', {'entities': [(71, 91, 'Port')]}), ('For those who don’t have the visibility, feel free to check out our free Scanmon system for port 37215 and 52869, or ISC port pages for 37215 and 52869.', {'entities': [(92, 112, 'Port')]}), ('As can be seen from the following picture, the bot will scan port 37215 and 52869 randomly, determined by the remainder of a random integer mod 3.', {'entities': [(61, 81, 'Port')]}), ('During the scanning, Satori will utilize two different exploits, one on port 37215, while the other on 52869.', {'entities': [(72, 82, 'Port'), (103, 108, 'Port')]}), ('The one on port 37215 is not fully disclosed yet, our team has been tracking this in the last few days and got quite some insight, but we will not discuss it here right now.(stay tuned for our update later).', {'entities': [(11, 21, 'Port')]}), ('For example, during last recent 12 hours we have seen 263,250 different IPs scanning port 37215, and 19,403 IPs scanning port 52869.', {'entities': [(85, 95, 'Port'), (121, 131, 'Port')]}), ('We analyzed another Mirai variant called “Miori,” which is being spread through a Remote Code Execution (RCE) vulnerability in the PHP framework, ThinkPHP.', {'entities': [(82, 123, 'SV')]}), ('For its arrival method, the IoT botnet uses the said exploit that affects ThinkPHP versions prior to 5.0.23 and 5.1.31.', {'entities': [(74, 82, 'SV')]}), ('Our own analysis revealed that the cybercriminals behind Miori used the ThinkPHP RCE to make vulnerable machines download and execute their malware.', {'entities': [(72, 84, 'SV')]}), ('With Mirai Comes Miori: IoT Botnet Delivered via ThinkPHP Remote Code Execution Exploit.', {'entities': [(58, 79, 'SV')]}), ('Miori now spreading via Remote code execution vulnerability in', {'entities': [(24, 45, 'SV')]}), ('The Miori bot borrows the code from the dreaded Mirai malware and it first appeared in the threat landscape in late 2018 when the bot was spread by exploiting a ThinkPHP remote code execution vulnerability after the exploit code was made publicly available. ', {'entities': [(161, 205, 'SV')]}), ('Among the list of devices targeted by the Wicked Mirai are Netgear DGN1000 and DGN2200 v1 routers (also used by Reaper botnet).', {'entities': [(59, 74, 'Model'), (79, 97, 'Model')]}), ('Specifically, port 8080 brings an exploit for a flaw in Netgear DGN1000 and DGN2200 v1 routers (also used by the Reaper botnet).', {'entities': [(56, 71, 'Model'), (76, 86, 'Model')]}), ('On port 8080, the malware uses Netgear DGN1000 and DGN2200 v1 router exploits (also used by Reaper botnet).', {'entities': [(31, 46, 'Model'), (51, 68, 'Model')]}), ('If connected to Port 8080, the malware will use a remote code execution (RCE) Netgear exploit which works on DGN1000 and DGN2200 v1 routers, and is the same tool used by the Reaper botnet to compromise target machines.', {'entities': [(50, 77, 'SV'), (16, 25, 'Port'), (109, 116, 'Model'), (121, 139, 'Model')]}), ('On port 8080, Netgear DGN1000 and DGN2200 v1 router exploits are used, a CCTV-DVR remote code execution exploit is used on port 81, ', {'entities': [(3, 12, 'Port'), (14, 29, 'Model'), (34, 51, 'Model'), (82, 103, 'SV'), (123, 130, 'Port')]}), ('Below is a list of devices targeted by the Wicked Mirai; Port 8080: Netgear DGN1000 and DGN2200 v1 routers.', {'entities': [(57, 66, 'Port'), (68, 83, 'Model'), (88, 106, 'Model')]}), ('Devices Targeted by Wicked include Netgear DGN1000 and DGN2200 v1 routers on Port 8080.', {'entities': [(35, 50, 'Model'), (55, 73, 'Model'), (77, 86, 'Port')]}), ('The dissection of this suspicious file, known by Symantec as Trojan.Emotet, shows common elements such as: TCP communication over ports 80, 8080, 22,990.', {'entities': [(130, 152, 'Port')]}), ('Emotet connects to C2 servers on various ports including, but not limited to: 20, 80, 443, 7080, 8443, and 50000', {'entities': [(78, 112, 'Port')]}), ('We can see that port 80 returns the same universal 404 error as the hacked server did on the Emotet port, so most likely this is the port it forwards traffic to.', {'entities': [(16, 23, 'Port')]}), ('The C2 servers can receive these communications on port 80, which is the default port for HTTP, but may also receive them on port 443, which is the default for HTTPS traffic, or on a number of other nonstandard ports, including but not limited to 7080, 8080, 8090, 50000, or several others. ', {'entities': [(51, 58, 'Port'), (247, 270, 'Port')]}), ('The initial executable appears to launch an application application lpiograd.exe, seen in Figure 2 and then looks to make outbound network connections on port 80, to a single command and control (CnC) server', {'entities': [(154, 161, 'Port')]}), ('Emotet Trojan used commonly used port for communication (e.g TCP port 80, 8080, 443, 8443, 7080, 20, 22, 53)', {'entities': [(61, 107, 'Port')]}), ('Apart from this, several Mirai malware various are being distributed by exploiting the same ThinkPHP RCE vulnerability.', {'entities': [(101, 104, 'SV')]}), ('Cybercriminals are exploiting a ThinkPHP vulnerability — one that was disclosed and patched in December 2018 — for botnet propagation by a new Mirai variant we’ve called Yowai and Gafgyt variant Hakai.\xa0', {'entities': [(32, 40, 'Model')]}), ('Cybercriminals use websites created using the PHP framework to breach web servers via dictionary attacks on default credentials and gain control of these routers for distributed denial of service attacks\xa0', {'entities': [(46, 49, 'Model')]}), ('The Hakai (detected by Trend Micro as BACKDOOR.LINUX.HAKAI.AA) sample we observed explored flaws that may have remained unpatched in systems and added exploits for vulnerabilities in ThinkPHP.', {'entities': [(183, 191, 'Model')]}), ('The remote code execution (RCE) vulnerability allows threat actors to infect machines based on the Linux operating system and execute Miori, which then generates a notification on the victim’s console.', {'entities': [(4, 31, 'SV')]}), ('Security researchers discovered a new variant of Mirai malware known as Miori that is targeting internet of things (IoT) devices to integrate into a larger botnet and launch distributed denial-of-service (DDoS) attacks. Trend Micro noted that the threat, which was first identified in early December, takes advantage of an exploit in the ThinkPHP programming framework.\xa0', {'entities': [(338, 346, 'Model')]})]

def train_spacy(data,iterations):
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
       

    # add labels
    for _, annotations in TRAIN_DATA:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


prdnlp = train_spacy(TRAIN_DATA, 20)

# Save our trained Model
modelfile = input("Enter your Model Name: ")
prdnlp.to_disk(modelfile)

#Test your text
test_text = input("Enter your testing text: ")
doc = prdnlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)