Руководство по источнику
Этот текст представляет собой содержимое конфигурационного файла сетевого хранилища Synology, который служит центральным узлом для определения системных параметров и доступных функций устройства. В нем зафиксированы как технические ограничения, такие как максимальное количество учетных записей и дисков, так и региональные настройки, включая часовой пояс и язык интерфейса. Значительная часть данных посвящена управлению сервисами, где активируются протоколы передачи файлов, правила безопасности и параметры уведомлений через SMS или электронную почту. По сути, данный документ является цифровым паспортом системы, координирующим работу аппаратного обеспечения и программной оболочки для обеспечения стабильной работы сервера.











firstuser@DiskStation:~$ cat /etc/synoinfo.conf unique="synology_88f6281_212j" company_title="Synology"
system options
timezone="Amsterdam" language="def" maillang="enu" codepage="enu" defquota="5" defshare="public" defgroup="users" defright="writeable" configured="yes" pswdprotect="no" autoblock_expriedday="0" autoblock_attempts="5" autoblock_attempt_min="60" supportmysql="yes" supportquota="yes" supportitunes="yes" supportddns="yes" supportfilestation="yes" supportssh="yes" supportNFS="yes" supportNFSKerberos="yes" supportrsrcmon="yes" supportmemtest="yes" supportmount="yes" support_fw_security="yes" support_directory_service="yes" support_power_schedule="yes" support_buzzer="yes" support_poweroff="yes" supporttrustdomain="yes" support_ipsec="yes" supportMFP="yes" support_synoacl="yes" support_wireless="yes" support_wireless_number="2" supportMTU="yes" supportrcpower="yes" supportext4="yes" supporthfsplus="yes" support_wimax="yes" showdisktemperature="yes" support_mtd_serial="yes" support_auto_poweron="yes" support_synopkg="yes" supportsmart="yes" supportntfswrite="yes" support_share_encryption="yes" mfp_manualtimer="300" mfp_autotimer="60" buzzeroffcfg="0x8" supportfileindex="yes" disk_warning_percent="0.1" disk_inode_warning_percent="0.05" esata_disk_warning_percent="0.1" esata_partition_warning_percent="0.1" usb_disk_warning_percent="0.05" usb_partition_warning_percent="0.05" sdcard_warning_percent="0.05" sdcard_partition_warning_percent="0.05" supportTc="yes" supportVLAN="yes" support_iscsi_target_block="yes" support_iscsi_target="yes" support_iscsi_lunbkp="yes" support_postgresql_data_checksums="no" support_power_recovery="yes" support_group="yes" support_app_privilege="yes" support_s2s_server="yes" support_task_scheduler="yes" support_disk_report="yes" support_sys_time="yes" support_storage_mgr="yes" support_disk_msgr="yes" retain_admin_pwd="no" support_ez_internet="yes"
service options
ftpport="21" syslogport="514" ftp_trans_ext_ip="no" ftpflowcontrol="no" ftpmaxuploadrate="0" ftpmaxdownloadrate="0" ftpanonymouslogin="no" ftpsupportutf8="yes" ftp_use_utf8="no" diskcache="on" standbytimer="60" standby_force="yes" auto_poweroff_timer="0" enableguest="no" usbbkp="yes" usbcopy="no" netbkp="yes" supportmediaservice="yes" runmediaservice="no" supportups="yes" ddns_update="no" ddns_select="TwoDNS.de" ddns_reclaim_interval_mins="3" portmap_admin="no" portmap_ftp="no" portmap_http="no" portmap_http_add="no" portmap_netbkp="no" portmap_netbkp_encrypt="no" php_openbasedir_customize="no" #run_bonjour_printer_service="yes" printer_driver_host="https://download.synology.com/airprint/DSM6.0/latest" supportstartupd="yes" supportdomain="yes" supportldap="yes" supportsnapshot="yes" supportvideostation="yes" support_audio="yes" support_s2s="yes" support_timebkp_server="yes" support_img_backupd="yes" enableRCPower="yes"
service limitations
maxaccounts="512" maxgroups="128" maxshares="256" maxdisks="2" maxprinters="2" maxlogsize="64"
UI options (limitations)
company="synology" supplang="enu,cht,chs,krn,ger,fre,ita,spn,jpn,dan,nor,sve,nld,rus,plk,ptb,ptg,hun,trk,csy" product="DiskStation" manager="Synology DiskStation" vender="Synology Inc." mailfrom="Synology DiskStation" updateurl="http://www.synology.com/" win98autodisconnect="yes" supportdcacheui="yes"
wins="none" AppleTalk="eth0"
hostname="DiskStation" ntpdate_period="daily" ntpdate_server="time.google.com" ntpdate_server_backup=""
sdkversion="no" allowanonymous="yes"
defaultfs="ext4" systemfs="ext4" addport="no" supportuart2="yes"
SMS options
smsserver="clickatell" smsport="80" smstemplate="https://api.clickatell.com/http/sendmsg?user=@@USER@@&password=@@PASS@@&api_id=3148203&to=@@PHONE@@&text=@@TEXT@@" smssepchar="+" smsuser="" smspass="" smsphone1="" smsphone2="" smsssl="yes" smstest="no" smsneedinterval="no" smsinterval="1"
VS60 options
vs_version="1.1"
DSM auto update default server
rss_server="http://update.synology.com/autoupdate/genRSS.php" rss_server_ssl="https://update.synology.com/autoupdate/genRSS.php"
Push Service Server address
pushservice_server="https://sns.synology.com/api/" pushbrowser_server="https://notification.synology.com/web/"
Redirect Server address
redirect_server="https://gofile.me/"
package_update_channel="beta"
pkg_source_trust_level="2"
update_server="http://update.synology.com/"
#allowed urls for iframe embed, separate by ',' frame_options_built_in_allow_url="find.synology.com/,gofile.me/" frame_options_deny_url=""
#prevent csrf attack enable_syno_token="yes" token_invalid_referer="fbsharing,fbdownload" token_valid_user_agent=""
#DSM Update type upgradetype="security"
#DSM Small Update URL small_info_path="https://update.synology.com/smallupdate"
#Help Online URL online_help_base_url="http://www.synology.com/"
password rules turn on by default
strong_password_enable="yes"
default dsm timeout
dsmtimeout="3600"
open arp_ignore and interface policy routing by default
arp_ignore="yes"
Bitmap for Fan debug mode, bit 0 means internal fan debug, bit 1 means external fan debug
enable_fan_debug="0x0"
Add key for support fan model
support_fan="yes"
Disk options
BS_Thr_Enable="yes" BS_Thr_Value="50"
remain_life_thr_enable="yes" remain_life_thr_value="5"
support_ihm="yes" upnpmodelurl="" upnpmodelname="DS212j" upnpmanufacturerurl="http://www.synology.com/" runupnp="no" upnpfriendlyname="DiskStation Device" upnpdevicetype="DiskStation" upnpmodeldescription="DiskStation UPnP Device" s2s_watches_max="102400" timebkp_max_task="2" support_syno_hybrid_raid="yes" maxservices="64" support_fan_adjust_dual_mode="yes" satadeepsleeptimer="1" is_business_model="no" esataportcfg="0x0" iscsi_target_type="lio" synobios="ds212j" sata_deep_sleep_en="yes" vpn_conn_max="5" buzzeroffen="0x1f" support_tutorial="yes" supportraid="yes" internalportcfg="0x3" usbportcfg="0x30000" max_iscsiluns="10" max_iscsitrgs="10" surveillance_camera_max="5" fantime="1" s2s_task_max="2" max_volumes="256" support_autocreate_shr="yes" max_lunbkp_srv="1" eth0_mtu="1500" support_net_topology="no" install_agent="dsassistant" upgrade_pkg_dsm_notification="yes" upgrade_pkg_email_notification="no" dns_mode="static" usb_standbytimer="30" dsm_autoupdate_type="download" enable_data_collect="no" theme="business" welcome_hide="yes" net_topology="client" portcheck="yes" pkg_def_intall_vol="" thumb_conv_paused="yes" thumb_conv_resume_time="-1" ftpanonymouschroot="no" ftplowport="0" ftphighport="0" ftpmaxconnperip="0" ftpxferlog="yes" ftp_enable_fxp="no" ftpUserChroot="no" service_fw_target_interface="all" smtp_mail_enabled="yes" sendnewusermail="no"
Fixed items
ss_cms="yes" supportsurveillance="yes" ss_vs="yes" ss_sync_event_player="yes"
Fixed items
Fixed items
support_disk_hibernation="yes" supportphoto="yes" supportphotopersonal="yes"
Fixed items
smbxferlog="yes" pkg_enable_paypal="no" enable_pkg_autoupdate_all="no" fan_config_type_internal="high"
Fixed items
custom_login_title="" login_style="light" login_logo_customize="no" login_background_customize="no" login_only_bgcolor="yes" login_welcome_title="" login_welcome_msg="" login_version_logo="no" disk_wakeup_log_en="yes"
Fixed items
Fixed items
disable_volumes="" pushservice_mail_account="anokhin.sergey@gmail.com" pushservice_ds_info_updated="yes" pushservice_dstoken="FQJlWSQI6xn9SuLDTCnL7Cs" pushservice_dsserial="C9KON02643" pushservice_mail_account_updated="yes" pushservice_mail_enabled="yes" pushservice_mobile_enabled="yes" pushservice_last_sending_time="1778044412" pushservice_sending_interval="60" sftpPort="22"
Fixed items
Fixed items
udc_check_state="6.1.7"
Fixed items
pkg_term_version="0001"
Fixed items
Fixed items
forget_password_enable="no" otp_enforce_option="none" enable_homeshare_recyclebin="no" userHomeEnable="yes"
Fixed items
Fixed items
Fixed items
Fixed items
login_background_color="#FFFFFF"
Fixed items
support_download="yes"
enable_hibernation_debug="yes" hibernation_debug_level="1" firstuser@DiskStation:~$