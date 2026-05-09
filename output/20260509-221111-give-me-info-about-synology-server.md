---
date: 2026-05-09 22:11
---

# give me info about synology server

## Answer

**Device:** [[Synology DS212j]] — NAS из линейки 2012 года, используется как домашний бэкап-сервер.

### Железо

| Параметр | Значение |
|---|---|
| Модель | DS212j |
| Серийный номер | C9KON02643 |
| CPU | MARVELL Kirkwood 88F6281, 1.2 GHz, 1 ядро |
| RAM | 256 MB |
| Дисков макс. | 2 (RAID-1) |
| IP | 192.168.1.99 |
| WOL MAC | 00:11:32:16:b0:6b |

### Программное обеспечение

- **ОС:** [[DSM]] 6.1.7-15284 Update 3 (legacy-ветка; DS212j не поддерживает DSM 7)
- **SSH:** OpenSSH 6.8p1-hpn14v6, ключ `claude-synology` (ED25519)
- **NTP:** time.google.com, часовой пояс GMT+01:00
- **Pushservice:** ivanoff.sergey@gmail.com

### Шары

| Шара | Назначение |
|---|---|
| `dump` | VM-дампы из Proxmox |
| `HomeAssistant` | Бэкапы Home Assistant |
| `Obsidian` | Синхронизация Obsidian vault |
| `VMware` | Снапшоты VMware |

### Подключённые хосты

| Хост | IP | Протокол | Назначение |
|---|---|---|---|
| Proxmox | 192.168.1.99 | SMB → NFS | Бэкапы VM |
| Home Assistant | 192.168.1.92 | SMB | Бэкапы HA |

### Ключевые процессы DSM

| Сервис | Процесс | Роль |
|---|---|---|
| SMB | `smbd` | Файловый шаринг; блокирует гибернацию HDD |
| Логирование | `syslog-ng` | Непрерывная запись на диск |
| Статистика | `synologaccd` | Пишет `.SYNOACCOUNTDB` |
| Отладка гибернации | `syno_hibernation_debug` | Диагностика сна |

Конфигурация — `/etc/synoinfo.conf`. Логи гибернации — `/var/log/hibernation.log` и `/var/log/hibernationFull.log`.

### Ограничения

Устройство ограничено железом 2012 года (256 MB RAM, 1 ядро). DS212j не поддерживает DSM 7. CloudSync был удалён из-за сбоев аутентификации.

> **Замечание:** в вики есть мёртвые ссылки `[[HDD Hibernation]]` из [[Synology DS212j]] и [[DSM]], но страница этой концепции отсутствует.
