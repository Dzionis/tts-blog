# AIDente Blog

SEO-блог для приложения [AIDente - AI Calorie Counter](https://apps.apple.com/us/app/aidente-ai-calorie-counter/id6751173116).

Сайт: **aidente.net** · Стек: Jekyll + GitHub Pages · Деплой: автоматический при push в `main`

---

## Быстрый старт: добавить новую статью

### Способ 1 — Slash-команда в Claude Code (рекомендуется)

Открой VSCode с Claude Code и введи в чате:

```
/new-post тема статьи | primary keyword
```

**Примеры:**

```
/new-post how to count macros for weight loss | macro counting app
/new-post best protein foods for muscle gain | high protein foods
/new-post calorie deficit explained | calorie deficit for weight loss
/new-post intermittent fasting calorie tracking | intermittent fasting calories
```

Claude сгенерирует статью и **сам сохранит файл** в `_posts/`. Затем:

```bash
git add _posts/
git commit -m "Add: [название статьи]"
git push
```

Через ~2 минуты статья появится на сайте автоматически.

---

### Способ 2 — Python скрипт из терминала

Требует установленного и авторизованного Claude Code CLI (`claude`).

```bash
# Из корня проекта:
python scripts/generate_article.py \
  --topic "how to track calories when eating out" \
  --keyword "tracking calories restaurant"

# С указанием папки:
python scripts/generate_article.py \
  --topic "best foods for weight loss" \
  --keyword "weight loss foods" \
  --output _posts/
```

Скрипт вызывает `claude --print` под капотом — никаких API ключей не нужно.

После генерации:

```bash
git add _posts/
git commit -m "Add: new article"
git push
```

---

## Деплой

Деплой происходит **автоматически** при каждом `git push` в ветку `main` через GitHub Actions.

Статус деплоя: вкладка **Actions** в репозитории на GitHub.

**Первоначальная настройка GitHub Pages** (один раз):
1. Открой репозиторий на GitHub
2. Settings → Pages → Source → выбери **"GitHub Actions"**
3. Запушь код — сайт задеплоится автоматически

---

## Идеи для статей

SEO-запросы, под которые стоит писать:

| Тема | Keyword |
|------|---------|
| Как считать калории без весов | calorie counting without scale |
| Лучшие продукты с высоким белком | high protein low calorie foods |
| Что такое дефицит калорий | calorie deficit explained |
| Как похудеть не считая калории | how to lose weight without counting calories |
| Трекер калорий для начинающих | calorie tracker for beginners |
| AI vs ручной трекинг | AI calorie tracking vs manual |
| Макросы для похудения | macros for weight loss |
| Как отслеживать питание в ресторане | tracking calories eating out |
| Лучшие приложения для похудения | best weight loss apps iPhone |
| Калории в домашней еде | how to track homemade meals calories |

---

## Структура проекта

```
aidente-blog/
├── _config.yml          # Настройки Jekyll, app_store_url
├── _layouts/            # Шаблоны страниц
│   ├── default.html     # Базовый HTML
│   ├── post.html        # Шаблон статьи (с CTA блоком)
│   └── page.html        # Шаблон страницы
├── _includes/           # Переиспользуемые части
│   ├── header.html
│   ├── footer.html
│   └── seo-head.html    # SEO теги + Smart App Banner
├── _posts/              # Статьи блога (YYYY-MM-DD-slug.md)
├── assets/css/main.css  # Весь CSS
├── index.html           # Лендинг
├── blog/index.html      # Листинг статей
├── scripts/
│   └── generate_article.py  # Генератор статей через Claude CLI
├── .claude/commands/
│   └── new-post.md      # /new-post slash-команда
├── .github/workflows/
│   └── deploy.yml       # Auto-deploy на GitHub Pages
└── CNAME                # aidente.net
```

---

## Формат статьи

Каждый файл в `_posts/` — это Markdown с Jekyll front matter:

```markdown
---
layout: post
title: "Заголовок статьи"
description: "Мета-описание до 155 символов"
date: 2026-04-09 10:00:00 +0000
categories: [nutrition]
author: AIDente Team
---

Текст статьи...

## Start Tracking with AIDente

Финальный абзац про приложение (ссылку не нужно — layout добавит кнопку автоматически).
```

Допустимые категории: `nutrition`, `apps`, `weight-loss`, `recipes`
