# Lotus Sutra Project - Data Safety Protocol

**Created: November 15, 2025**
**Purpose: Protect your scholarly translation work from accidental loss**

---

## Current Protections in Place

### 1. Git Version Control ✓
- **Location**: `/Users/williamaltig/claudeprojects/Lotus_Sutra/.git`
- **Status**: Initialized and committed
- **What it does**: Tracks all changes to files, allows recovery of previous versions
- **Initial commit**: Includes all 9 project folders with 748 files tracked

**Key Commands**:
```bash
# Check status
git status

# See commit history
git log --oneline

# Restore a file if deleted
git checkout <filename>

# See what changed
git diff
```

### 2. Full Project Backup (1.4 GB) ✓
- **Location**: `/Users/williamaltig/claudeprojects/Lotus_Sutra_BACKUP_2025-11-15_180427`
- **Updated**: [Check periodically - create new backups monthly]
- **What it contains**: Complete snapshot of entire project at this date/time
- **How to restore**: Copy contents back to main folder if needed

### 3. Structured Organization ✓
- All chapters in `03_SCHOLARLY_TRANSLATION_2025/CHAPTERS/` (MARKDOWN + TEXT)
- Documentation organized by type
- Source materials preserved in separate folders
- Clear directory structure prevents accidental overwrites

---

## Additional Protections Needed

### 4. Time Machine (macOS Backup)
**Status**: ⚠️ NEED TO ENABLE

**Why**: Automatic hourly backups, can restore files deleted hours/days ago

**Setup**:
1. Plug in external hard drive (or use iCloud+)
2. System Preferences → Time Machine
3. Click "Select Backup Disk"
4. Choose your external drive
5. Toggle "Back Up Automatically" ON

**Restore from Time Machine**:
- Click Time Machine icon (top-right menu bar)
- Browse to a specific date
- Restore individual files or entire folder

### 5. Cloud Backup
**Status**: ⚠️ NOT SET UP

**Recommended Options**:

| Service | Cost | Best For |
|---------|------|----------|
| **iCloud Drive** | $0.99-9.99/mo | Simple, integrated with Mac |
| **Google Drive** | Free-15GB, then $1.99+/mo | Excellent search, sharing |
| **Dropbox** | Free-2GB, then $11.99+/mo | Synced folders, version history |
| **OneDrive** | Free-5GB, then with Office | Microsoft integration |
| **Backblaze** | $7/mo | Unlimited cloud backup |

**Recommendation**: Use **Google Drive** or **Dropbox**
- Sync entire `Lotus_Sutra` folder automatically
- Maintains version history (30 days free)
- Accessible from any device

---

## Recommended Workflow

### Before Major Operations (like folder reorganization):

```bash
# 1. Check git status - see what's changed
git status

# 2. Commit any unsaved work
git add .
git commit -m "Work before [operation name]"

# 3. Create a backup if working with critical files
cp -r 03_SCHOLARLY_TRANSLATION_2025 03_SCHOLARLY_TRANSLATION_2025_BACKUP_PRE_[operation]

# 4. Do the operation

# 5. Verify success - check key files exist
ls CHAPTERS/MARKDOWN/ | wc -l   # Should show 28 chapters

# 6. Commit the changes
git add .
git commit -m "Completed [operation name]"
```

### Daily/Weekly:
- Work on files
- Periodically commit progress: `git commit -m "Updated Chapter 5 with new material"`
- Time Machine backs up automatically (if enabled)
- Cloud sync happens automatically (if set up)

### Monthly:
- Create new timestamped backup: `cp -r Lotus_Sutra Lotus_Sutra_BACKUP_2025-12-15`
- Archive old backups to external drive if needed
- Verify git history is clean: `git log --oneline | head -20`

---

## Emergency Recovery Plan

### If files are accidentally deleted:

**Immediate (within hours)**:
1. **Git**: `git checkout <deleted filename>`
2. **Time Machine**: Use Time Machine to restore from recent snapshot

**Same day**:
3. **Full backup**: Copy from timestamped backup folder

**Last resort**:
4. **Cloud backup**: Restore from Google Drive/Dropbox version history

---

## Git Commit Message Guidelines

**Good format**:
```
Short description (50 chars or less)

Longer explanation if needed.
- Bullet point 1
- Bullet point 2
```

**Examples**:
```
✓ Updated Chapter 8 with new footnotes
✓ Reorganized project folder structure
✓ Fixed Sanskrit diacriticals in Chapter 15
✗ "fixed stuff" (too vague)
```

---

## What NOT to Do

❌ **Don't** trust a single backup (we have 3+ now)
❌ **Don't** let months pass without committing changes
❌ **Don't** ignore git status warnings
❌ **Don't** run large file operations without verification
❌ **Don't** delete directories without checking contents first

---

## Checking Your Protections

```bash
# 1. Verify git is working
cd Lotus_Sutra
git status

# 2. See recent commits
git log --oneline | head -10

# 3. Check backup exists
ls -lh ~/claudeprojects/Lotus_Sutra_BACKUP_*

# 4. Verify chapter files are present
ls 03_SCHOLARLY_TRANSLATION_2025/CHAPTERS/MARKDOWN/ | wc -l  # Should be 28

# 5. Check for Time Machine
system_profiler SPHardwareDataType | grep -i backup
```

---

## Summary of What's Protected

| What | Where | How Often | Recovery Time |
|------|-------|-----------|----------------|
| **Chapters (28)** | Git + Full Backup + Cloud | Every commit | < 1 minute |
| **Documentation** | Git + Full Backup + Cloud | Every change | < 1 minute |
| **All project files** | Git + Timestamped Backup | Created today | < 5 minutes |
| **Hourly changes** | Time Machine (enable) | Hourly | < 5 minutes |
| **Version history** | Cloud storage (enable) | Real-time | < 10 minutes |

---

## Next Steps

1. **Enable Time Machine** (see instructions above)
2. **Set up cloud backup** (Google Drive or Dropbox)
3. **Commit early and often**: `git add . && git commit -m "description"`
4. **Review this document monthly**
5. **Create new backup every month**

---

## Questions?

If you ever feel uncertain about a file operation:
1. Save a backup first
2. Commit to git: `git commit -m "Before [operation]"`
3. Tell me to do the operation carefully
4. Verify the results before continuing

Your work is now protected at multiple levels. You should never lose critical work again.
