from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time
import logging

f = open('index.html','rb')
data = f.read()
f.close()

class Resquest(BaseHTTPRequestHandler):
    def _set_response(self):
        self.sys_version="360 web server, 792/71644 HTTP Server version 2.0 - TELDAT S.A., A10WS/1.00, ADB Broadband HTTP Server, ADH-Web, AR, ASUSTeK UPnP/1.0 MiniUPnPd/1.4, ATS/5.3.0, Adaptec ASM 1.1, AirTies/ASP 1.0 UPnP/1.0 miniupnpd/1.0, Allegro-Software-RomPager/4.06, AmirHossein Server v1.0, AnWeb/1.42p, Android Webcam Server, AnyStor-E, Apache-Coyote/1.1, Apache/2.2.15 (CentOS), Apache/2.4.29 (Ubuntu), Apache/2.4.6 (Red Hat Enterprise Linux) PHP/7.3.11, Apache/2.4.6 (Red Hat Enterprise Linux) mod_jk/1.2.46 OpenSSL/1.0.2k-fips, App-webs/, ArGoSoft Mail Server Pro for WinNT/2000/XP, Version 1.8 (1.8.9.4), AvigilonGateway/1.0 Microsoft-HTTPAPI/2.0, Avtech, Baby Web Server, BigIP, BlueIris-HTTP/1.1, Boa/0.93.15, Boa/0.94.13, Boa/0.94.14rc20, Boa/0.94.14rc21, Boa/0.94.7, BolidXMLRPC/1.10 (Windows NT) ORION-BOLID v1.10, BroadWorks, Brovotech/2.0.0, CJServer/1.1, CPWS, CVM, Caddy, Cam, Cambium HTTP Server, Camera Web Server, CentOS WebPanel: Protected by Mod Security, Check Point SVN foundation, Cherokee/1.2.101 (Ubuntu), CherryPy/2.3.0, CherryPy/3.1.0beta3 WSGI Server, CherryPy/8.1.2, CirCarLife Scada v4.2.3, Cirpark Scada v4.5.3-rc1, Cisco AWARE 2.0, Citrix Web PN Server, Commvault WebServer, Control4 Web Server, CouchDB/1.6.1 (Erlang OTP/18), CouchDB/1.6.1 (Erlang OTP/R16B03), CouchDB/2.0.0 (Erlang OTP/17), Cougar/9.01.01.3841, Cougar/9.01.01.5001, Cowboy, Cross Web Server, D-Link Web Server 0.01, DNVRS-Webs, DVR-HttpServer/1.0, DVRDVS-Webs, DWS, DasanNetwork Solution, Debian/4.0 UPnP/1.0 miniupnpd/1.0, Deluxe Beauty Office, Destiny, DpmptspKarawangkab_HTTP_SERVER, E2EE Server 1.0, EBox, EShare Http Server/1.0, Easy-Web Server/1.0, Embedded HTTP Server., Embedded HTTPD v1.00, 1999(c) Delta Networks Inc., Embedthis-Appweb/3.2.3, Embedthis-Appweb/3.3.1, Embedthis-http, Entrust, Ericom Access Server, Ericom Access Server x64, FN-Httpd 1.0 [HTTP/1.1], FUJITSU ServerView iRMC S4 Webserver, FileMakerPro/6.0Fv4 WebCompanion/6.0v3, Flussonic, GSHD/3.0, GeoHttpServer, GeoWebServer 4.4.1.0, Ginatex-HTTPServer, GlassFish Server Open Source Edition 4.0, GoAhead-Webs, GoAhead-Webs/2.5.0, GoAhead-http, GoTTY, H3C-Miniware-Webs, HFS 2.2f, HFS 2.3 beta, HFS 2.3e, HFS 2.3i, HFS 2.3k, HFS 2.3m, HTTP Server, HTTP Server 1.0, HTTP Software 1.1, HTTPD, HTTPD Web Server, HTTPD-HR Server powered by Apache, HTTPD_gw 1.0, Hikvision-Webs, Hipcam, HostGW.com EnterpriseServer built fo SMKN 1 Kaligondang, Http Server, Httpd, Httpd/1.0, Hydra/0.1.8, IBM_HTTP_Server, IIS, IP Webcam Server, IPC@CHIP, IPCamera-Webs, IPCamera-Webs/2.5.0, IPCamera_Logo, IPOffice/, IceWarp/12.1.1.4 x64, IceWarp/9.4.2, IdeaWebServer/0.83.292, If you want know, you can ask me, Indy/9.0.11, Intoto Http Server v1.0, InvalidPanda/1.0.0, JAWS/1.0, JAWS/1.0 Jan 21 2017, JBoss-EAP/7, JDVR/4.0, JFinal 4.5, JWS, Jetty(6.1.19), KMS_ACCESS, Keil-EWEB/2.1, Kerio MailServer 6.5.2, Kestrel, LINUX-2.6 UPnP/1.0 MiniUPnPd/1.5, LTE Router Webs, Lanswitch - V100R003 HttpServer 1.1, Linux, HTTP/1.1, DIR-860L Ver 1.01, Linux/2.6.18 UPnP/1.0 miniupnpd/1.0, Linux/2.x UPnP/1.0 Avtech/1.0, Linux/3.10.0 eHomeMediaCenter/1.0, Linux/3.10.104 eHomeMediaCenter/1.0, Linux/3.10.33 UPnP/1.0 Teleal-Cling/1.0, Linux/3.14.29 CyberHTTP/1.0, Linux/3.4.39 UPnP/1.0 Cling/2.0, LiteSpeed, Lotus-Domino, MIPS LINUX/2.4 UPnP/1.0 miniupnpd/1.0, MJPG-Streamer/0.2, MS-SDK-HttpServer/1.0, MailEnable-HTTP/5.0, Mars, Mathopd/1.5p6, Mbedthis-AppWeb/2.0.4, Mbedthis-Appweb/12.5.0, Mbedthis-Appweb/2.4.0, Mbedthis-Appweb/2.4.2, Microsoft-HTTPAPI/1.0, Microsoft-HTTPAPI/2.0, Microsoft-IIS/10.0, Microsoft-IIS/5.0, Microsoft-IIS/5.1, Microsoft-IIS/6.0, Microsoft-IIS/7.0, Microsoft-IIS/7.5, Microsoft-IIS/8.0, Microsoft-IIS/8.5, Microsoft-NetCore/2.0, UPnP/1.0 DLNADOC/1.50, Microsoft-WinCE/7.00, Mikrotik HttpProxy, Mini Embedded Web Server, Mini web server 1., Mini web server 1.0 ZTE corp 2005., Mini web server 1.0 ZXIC corp 2005., MiniServ/1.890, MistServer/2.14.2, MochiWeb/1.0 (Any of you quaids got a smint?), MonitorServer/0.10.5.363 Python/2.7.5, Monitorix HTTP Server, Monkey, Mono-HTTPAPI/1.0, MoxaHttp/1.0, Mrvl-R1_0, Mrvl-R2_0, NISS, NVR EXT SERVER, NVR Webserver, Net-OS 5.xx UPnP/1.0, NetBox Version 2.8 Build 4128, NetEVI/3.10, Netwave IP Camera, Network Camera with Pan/Tilt, Network_Module/1.0 (WXA-50), Nexus/3.13.0-01 (OSS), Nexus/3.9.0-01 (OSS), Nginx, Nginx Microsoft-HTTPAPI/2.0, Nucleus/4.3 UPnP/1.0 Virata-EmWeb/R6_2_0, OPNsense, OceanView-CDN, Oktell LS, OpenBCM/1.07b3, OpenBSD httpd, Oracle Containers for J2EE, Oracle GlassFish Server 3.1.2.2, Oracle XML DB/Oracle Database, Oracle-Application-Server-10g/10.1.2.0.2 Oracle-HTTP-Server, Oracle-Application-Server-11g, Oracle-HTTP-Server, Oracle-HTTP-Server-11g, Oracle_WebDb_Listener/2.1, PBX/63.0.2 (CentOS64), PRTG/19.3.51.2830, Pan/Tilt, PanWeb Server/ -, Payara Server 5.193 #badassfish, PrHTTPD Ver1.0, Proxy, Python/3.6 aiohttp/2.3.10, Qualvision -HTTPServer, REP Server, RNOAAA018180026 HTTP Server version 2.0 - TELDAT S.A., Rabbit, RapidLogic/1.1, Raption v5.8.0, ReeCam IP Camera, RemotelyAnywhere/9.0.856, Reposify, Resin/2.1.12, Resin/3.0.17, Resin/3.1.8, Rex/12.0.7601.17514, RomPager/4.07 UPnP/1.0, RomPager/4.51 UPnP/1.0, Router, Router Webserver, SAP, SCADA, SQ-WEBCAM, SRS/3.0.45(OuXuli), SY8033, SY8045, Safe3 Web Firewall, Safedog/4.0.0, ScreenConnect/19.4.25542.7213-2135886336 Microsoft-HTTPAPI/2.0, Serv-U/11.3.0.2, Server, ServiceNow, Servlet 2.5; JBoss-5.0/JBossWeb-2.1, Servlet/2.5 JSP/2.1, SimpleHTTP/0.6 Python/2.7.15+, SinforHttpd/1.0, SmartXFilter, SoftManager Application Server, SonicWALL, Spark, Start HTTP-Server/1.1, Sun GlassFish Enterprise Server v2.1.1, Swift1.0, Switch, SyncThru 5, TOPSEC, TP-LINK Router, TWebAP/2.1.2.9, Tas, Techno Vision Security System Ver. 2.0, Tengine/2.3.2, Thecapital Caphe Websphere 12.3 build 3.456.234.2600, This is webserver, TibetSystem Server 2.0, Tieline, Tntnet/2.1, Topsec, TornadoServer/6.0.2, TurnStat webserver, TwistedWeb/18.9.0, U S Software Web Server, UBNT Streaming Server v1.2, UCS PremieraExternal v4.0.4.24, UMC Webserver/5.0, UPnP/1.0 DLNADOC/1.50 Allwinnertech/0.1.0, UPnP/1.0 DLNADOC/1.50 Platinum/1.0.5.13, Unknown, Unspecified, UPnP/1.0, Unspecified, VAppServer/6.0.0, VB, VB100, VCS-VideoJet-Webserver, VPON Server/1.0, Varnish, Vinahost, Virata-EmWeb/R6_0_1, Virtual Web 0.9, Vivotek Network Camera, WAF, WCY_WEBServer/1.0, WCY_WEBServer/2.0, WDaemon/10.0.0, WDaemon/4.0, WEB SERVER, WMSServer/2.0.1.0, WN/2.4.7, WS CDN Server, WSGIServer/0.2 CPython/3.7.3, WWW Server/1.1, WWW-Kodeks/6.4, Warp/3.2.27, Warp/3.2.28, Waveplus HTTPD, Web Express 0.9, Web Server, Web Switch, Web server, Web-Server/3.0, WebServer, WebServer/1.0 UPnP/1.0, Webs, WebsServer/2.1.8 PeerSec-MatrixSSL/, Werkzeug/0.9.6 Python/2.7.6, WhatsUp, WhatsUp_Gold/8.0, WiJungle, WildDuck API, WildFly/10, WildFly/11, WildFly/8, WildFly/9, WindRiver-WebServer/4.7, WindWeb/1.0, Windows Server 2008 R2, UPnP/1.0 DLNADOC/1.50, Serviio/1.8, Wing FTP Server(Mario Kaserer), Wing FTP Server(MediaSend pty Ltd), Wing FTP Server/3.3.5(), Winstone Servlet Engine v0.9.10, Wisp/1.0.71.15, WowzaStreamingEngine/4.7.1, WowzaStreamingEngine/4.7.7, XDaemon v1.0, XEvil_4.0.0[Beta][V4_0b25], Xavante 2.2.0 embeded, Xitami, Yawcam, YouTrack, YxlinkWAF, ZK Web Server, ZSWS/2.2, ZTE web server 1.0 ZTE corp 2015., Zope/(2.13.15, python 2.7.3, linux2) ZServer/1.1, Zope/(2.13.27, python 2.7.3, linux2) ZServer/1.1, Zscaler/5.7, abcd, access to tenda, alphapd, alphapd/2.1.7, alphapd/2.1.8, antid, axhttpd/1.4.0, axhttpd/1.5.3, beegoServer:1.12.0, bots-webserver, box, build-in http server, calibre 4.0.0, ccapi-dvrs-production, cisco-IOS, cloudflare, cloudflare-nginx, cvmd-1.0.0 (r1), dcs-lig-httpd, de475d6363d3b9295c4645cd08294af288c1c0de, eHTTP v2.0, eboo server, embedded http dameon, falcon/2.1, foo, gSOAP/2.7, gen5th/1.33.00, gen5th/1.82.01, go1984, gunicorn/19.3.0, h2o/2.3.0-DEV@6cde7eb3f, http server 1.0, httpd, httpd/1.00, httpd/2.0, httpd_four-faith, httpserver, i-Catcher Console, iSpy, jjhttpd v0.1.0, kangle/3.5.8.2, kong/0.14.0, libwww-perl-daemon/6.01, lighttpd, lighttpd-Intelbras, lighttpd/1.4.28, lighttpd/1.4.35, lighttpd/1.4.43, lighttpd/1.4.54, localhost, lwIP/1.4.0 (http://savannah.nongnu.org/projects/lwip), mORMot (Windows) Microsoft-HTTPAPI/1.0, mORMot (Windows) Microsoft-HTTPAPI/2.0, micro_httpd, minhttpd, mini_httpd/1.19 19dec2003, mini_httpd/1.21 18oct2014, mini_httpd/1.30 26Oct2018, miniupnpd/1.0 UPnP/1.0, mysrv, nPerf/2.2.0 2019-04-02, nextgen_0.2, nginx, nginx/1.8.0, ngjit, nostromo 1.9.4, o2switch PowerBoost, openresty, product only, rchttpd/1.0, rednetcloud, scada, secure, siyou server, sky_router, squid, squid/3.1.18, staging, sthttpd/2.27.0 03oct2014, thttpd, thttpd-alphanetworks/2.23, thttpd/2.25b 29dec2003, thttpd/2.25b-lxc 29dec2003, thttpd/2.27 19Oct2015, tinyproxy/1.10.0, tsbox, uc-httpd 1.0.0, uc-httpd/1.0.0, waitress, web, webcam 7, webcamXP, webserver, webserver/1.0, wfe, wfust, wildix-http-server, wizzardo-http/0.1, yawcam"
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header("Via", "1.1 50766bfb56389c696c1525db90e16f23.cloudfront.net (CloudFront)")
        self.send_header("X-ac", "3.bur _bur")
        self.send_header("X-Adblock-Key", "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANnylWw2vLY4hUn9w06zQKbhKBfvjFUCsdFlb6TdQhxb9RXWXuI4t31c+o8fYOv/s8q1LGPga3DE1L/tHU4LENMCAwEAAQ==_LvjToEEzlFo/9bgzGLRy9NYflonbd6rlWsuc2BxA52ZwpWZNNYovwHmcf/DNVDVQfVyZWew8CIk6q8+YCc9XFA==")
        self.send_header("X-Alternate-Cache-Key", "cacheable:ba92b39be043e3c90d2fd075057dd3e5")
        self.send_header("X-Amz-Cf-Id", "CtsEH7_KQ5yf2LQM4TNLiEjUavO2mWjwAez9sPj8Ws5MUdPUz-2G-g==")
        self.send_header("X-Amz-Cf-Pop", "MAA50-C1")
        self.send_header("X-App-Server", "app07")
        self.send_header("X-AspNet-Version", "4.0.30319")
        self.send_header("X-AspNetMvc-Version", "5.2")
        self.send_header("X-Backside-Transport", "FAIL FAIL")
        self.send_header("X-Cache", "miss")
        self.send_header("X-Cache-Enabled", "False")
        self.send_header("X-Cache-Group", "normal")
        self.send_header("X-Cache-Hits", "0")
        self.send_header("X-Cache-Lookup", "NONE from ezproxies.com:3128")
        self.send_header("X-Cache-Miss-From", "parking-74c5b8d946-dhmw5")
        self.send_header("X-Cacheable", "SHORT")
        self.send_header("X-Check", "3c12dc4d54f8e22d666785b733b0052100c53444")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("x-contextid", "KUgWEidx/01OfltCh")
        self.send_header("X-Dc", "gcp-us-east1,gcp-us-central1,gcp-us-central1")
        self.send_header("X-Download-Options", "noopen")
        self.send_header("X-Drupal-Cache", "HIT")
        self.send_header("X-Fastly-Request-ID", "ed15bdb8f4d9179ebe5b6b8441d6148a4a8e203f")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("X-Generator", "Drupal 7 (http://drupal.org)")
        self.send_header("X-GitHub-Request-Id", "2544:7F5D:24C5A8:296D36:5E212B7B")
        self.send_header("X-hacker", "If you're reading this, you should visit automattic.com/jobs and apply to join the fun, mention this header.")
        self.send_header("X-Iinfo", "11-40203780-0 0NNN RT(1579229728731 0) q(0 -1 -1 -1) r(0 -1)")
        self.send_header("X-Language", "english")
        self.send_header("X-LiteSpeed-Cache", "hit")
        self.send_header("X-Mod-Pagespeed", "1.13.35.2-0")
        self.send_header("X-nananana", "Batcache")
        self.send_header("X-Nginx-Cache-Status", "MISS")
        self.send_header("X-Page-Speed", "1.13.35.2-0")
        self.send_header("X-Permitted-Cross-Domain-Policies", "none")
        self.send_header("X-Pingback", "https://example.com/xmlrpc.php")
        self.send_header("X-Powered-By", "ASP.NET")
        self.send_header("X-Powered-By-Plesk", "PleskWin")
        self.send_header("X-Powered-CMS", "Bitrix Site Manager (30ebf3fe2d1251fbd7f82a700bcc1f66)")
        self.send_header("X-Proxy-Cache", "MISS")
        self.send_header("X-Redirect-By", "WordPress")
        self.send_header("X-Request-Id", "ecff8573-23ca-4dbc-a1a9-e8af7876c4ae")
        self.send_header("X-Robots-Tag", "none")
        self.send_header("X-Runtime", "0.009850")
        self.send_header("X-Seen-By", "6ivkWfREES4Y8b2pOpzk7CWfEJXUOf1J0Ah0dFlolkk=,sHU62EDOGnH2FBkJkG/Wx8EeXWsWdHrhlvbxtlynkVgTe3xZ//Nn3ncOxm4L8+OZ,2d58ifebGbosy5xc+FRaloPX4ngKfQM8fEHbwELHijmIqTfEHZn8YWW5uAXEQIRN,Nlv1KFVtIvAfa3AK9dRsI1LG4DohEKZjFvwGCeUAw4o=,2UNV7KOq4oGjA5+PKsX47FkEEikzl50vr1frqgW6QO0=,m0j2EEknGIVUW/liY8BLLk/s7xWBjZnTAAKbWiIaXHM=,1wy2ILu/S4rlWT/R4rqCrbwzwaTdV46v3H98eV9Tx1Y=,pglrwSJCjYpA6tXbCNiuHGONCeZnKft44mfcHgtbd+pIazm+iXfj+gQPTfEzrvhXZnxsoNoVOAEkuZjJ6GDELg==")
        self.send_header("X-Served-By", "cache-xsp21434-XSP")
        self.send_header("X-Server-Powered-By", "Engintron")
        self.send_header("X-ShardId", "80")
        self.send_header("X-ShopId", "25693290577")
        self.send_header("X-Shopify-Generated-Cart-Token", "aa0b6d68e41056d2955ae9e6fb516372")
        self.send_header("X-Shopify-Stage", "production")
        self.send_header("X-Sorting-Hat-PodId", "80")
        self.send_header("X-Sorting-Hat-ShopId", "25693290577")
        self.send_header("X-Squid-Error", "ERR_INVALID_URL 0")
        self.send_header("X-Src-Webcache", "fe05")
        self.send_header("X-Template", "tpl_CleanPeppermintBlack_twoclick")
        self.send_header("X-Timer", "S1579233183.306174,VS0,VE0")
        self.send_header("X-Turbo-Charged-By", "LiteSpeed")
        self.send_header("X-UA-Compatible", "IE=EmulateIE7")
        self.send_header("X-Varnish", "336777936")
        self.send_header("X-Varnish-Cache", "Miss")
        self.send_header("X-Wix-Request-Id", "1579229867.68013969302196914554")
        self.send_header("X-XSS-Protection", "1; mode=block")                
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        logging.info("Time: %s\nGET %s\nPath: %s\nHeaders:\n%s\n", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),str(self.client_address[0]), str(self.path), str(self.headers))
        self._set_response()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("Time: %s\nPOST %s\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  str(self.client_address[0]), str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()


def run(server_class=HTTPServer, handler_class=Resquest, port=8080):
    logging.basicConfig(level=logging.INFO,filename="fuwofo.log",filemode="a",format='%(message)s')

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()