#!/bin/bash
# Batch process all chapters 11-28

cd /Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters

echo "======================================================================"
echo "LOTUS SUTRA TTS OPTIMIZATION - CHAPTERS 11-28"
echo "======================================================================"
echo ""

# Chapter 11
echo "Processing Chapter 11..."
python3 ../simple_process_one.py "11_CHAPTER_WHEN_THE_JEWELED_TOWER_ROSE_UP.txt" "11_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 12
echo "Processing Chapter 12..."
python3 ../simple_process_one.py "12_CHAPTER_WHEN_YOUR_ENEMY_WAS_YOUR_TEACHER.txt" "12_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 13
echo "Processing Chapter 13..."
python3 ../simple_process_one.py "13_CHAPTER_WHEN_THE_ROAD_GETS_ROUGH,_YOU_GOTTA_KEEP_WALKING.txt" "13_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 14
echo "Processing Chapter 14..."
python3 ../simple_process_one.py "14_CHAPTER_HOW_TO_KEEP_YOUR_SOUL_CLEAN_WHEN_THE_WORLD'S_GONE_WRONG.txt" "14_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 15
echo "Processing Chapter 15..."
python3 ../simple_process_one.py "15_CHAPTER_WHEN_THE_UNDERGROUND_ARMY_ROSE_UP.txt" "15_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 16
echo "Processing Chapter 16..."
python3 ../simple_process_one.py "16_CHAPTER_HOW_LONG_THE_TATHĀGATA'S_BEEN_ALIVE.txt" "16_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 17
echo "Processing Chapter 17..."
python3 ../simple_process_one.py "17_CHAPTER_COUNTING_UP_THE_GRACE.txt" "17_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 18
echo "Processing Chapter 18..."
python3 ../simple_process_one.py "18_CHAPTER_THE_JOY_THAT_MULTIPLIES.txt" "18_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 19
echo "Processing Chapter 19..."
python3 ../simple_process_one.py "19_CHAPTER_WHEN_YOUR_SENSES_WAKE_UP.txt" "19_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 20
echo "Processing Chapter 20..."
python3 ../simple_process_one.py "20_CHAPTER_THE_BODHISATTVA_WHO_NEVER_LOOKED_DOWN.txt" "20_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 21
echo "Processing Chapter 21..."
python3 ../simple_process_one.py "21_CHAPTER_WHEN_THE_LORD_SHOWED_HIS_HAND.txt" "21_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 22
echo "Processing Chapter 22..."
python3 ../simple_process_one.py "22_CHAPTER_THE_PASSING_ON.txt" "22_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 23
echo "Processing Chapter 23..."
python3 ../simple_process_one.py "23_CHAPTER_MEDICINE_KING_BODHISATTVA_-_THE_STORY_OF_HOW_HE_GAVE_IT_ALL.txt" "23_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 24
echo "Processing Chapter 24..."
python3 ../simple_process_one.py "24_CHAPTER_WONDERFUL_SOUND_BODHISATTVA.txt" "24_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 25
echo "Processing Chapter 25..."
python3 ../simple_process_one.py "25_CHAPTER_THE_ONE_WHO_HEARS_THE_WORLD_CRYING.txt" "25_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 26
echo "Processing Chapter 26..."
python3 ../simple_process_one.py "26_CHAPTER_THE_PROTECTION_SONGS.txt" "26_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 27
echo "Processing Chapter 27..."
python3 ../simple_process_one.py "27_CHAPTER_THE_BEAUTIFUL_KING_AND_HIS_GOOD_FRIENDS.txt" "27_CHAPTER_OPTIMIZED.txt"
echo ""

# Chapter 28
echo "Processing Chapter 28..."
python3 ../simple_process_one.py "28_CHAPTER_UNIVERSAL_WORTHY_COMES_TO_ENCOURAGE_YOU.txt" "28_CHAPTER_OPTIMIZED.txt"
echo ""

echo "======================================================================"
echo "OPTIMIZATION COMPLETE"
echo "======================================================================"
echo ""
echo "All 18 chapters (11-28) have been optimized for Google AI Studio Gemini TTS."
echo "Optimized files are ready in:"
echo "/Users/williamaltig/claudeprojects/Lotus_Sutra/04_AUDIO_PRODUCTION/chapters/"
echo ""
