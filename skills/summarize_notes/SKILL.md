\---

name: Summarize Study Notes

description: Converts your messy class notes into clean summaries and quiz questions for quick revision

tags: \[summarization, notes, studying, review]

\---



\# Summarize Study Notes Skill



\## Description

This skill takes your lengthy study notes and converts them into concise, organized summaries. It extracts key concepts, creates flashcards, and organizes information for better retention.



\## Input Required

\- \*\*Subject\*\*: The subject of your notes

\- \*\*Notes\*\*: Your raw study notes (text or copied content)

\- \*\*Summary Length\*\*: Brief (50%), Medium (70%), or Detailed (100%)

\- \*\*Format\*\*: Bullet Points, Outline, or Flashcards



\## Output Provided

\- Concise summary of key concepts

\- Main points highlighted

\- Flashcard-ready Q\&A format

\- Important definitions

\- Organized by subtopics

\- Saved to data/summaries.json



\## How It Works

1\. User inputs their study notes

2\. Skill analyzes and identifies key concepts

3\. Removes unnecessary information

4\. Creates concise summary

5\. Generates flashcards for revision

6\. Organizes content by topics

7\. Stores summary in JSON file



\## Example Usage



\*\*Example 1\*\*: Subject: Data Structures \& Algorithms - Binary Search Trees

\- Notes: Your long BST lecture notes

\- Summary Length: Medium (70%)

\- Format: Flashcards

\- Result: 10 Q\&A pairs covering concepts



\*\*Example 2\*\*: Subject: Operating Systems - CPU Scheduling

\- Notes: Textbook chapter notes

\- Summary Length: Brief (50%)

\- Format: Bullet Points

\- Result: Core concepts in 5-7 points



\*\*Example 3\*\*: Subject: Python Programming - Control Flow

\- Notes: Tutorial notes and code snippets

\- Summary Length: Detailed (100%)

\- Format: Outline

\- Result: Complete hierarchy of topics



\*\*Example 4\*\*: Subject: Computer Networks - Network Layer

\- Notes: Lecture slides + notes

\- Summary Length: Medium (70%)

\- Format: Flashcards

\- Result: 15 important Q\&A pairs



\## Sample Output



\*\*Subject\*\*: Data Structures \& Algorithms

\*\*Topic\*\*: Sorting Algorithms

\*\*Summary Length\*\*: Medium

\*\*Format\*\*: Flashcards



FLASHCARD SUMMARY:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



Card 1:

Q: What is Sorting?

A: Arranging elements in a specific order (ascending/descending)



Card 2:

Q: What is Time Complexity of Quick Sort?

A: O(n log n) average case, O(n²) worst case



Card 3:

Q: Difference between Merge Sort and Quick Sort?

A: Merge Sort: Stable, O(n log n) always. Quick Sort: Unstable, faster in practice



Card 4:

Q: What is Bubble Sort's Time Complexity?

A: O(n²) in all cases - Simple but slow for large data



Card 5:

Q: When to use Insertion Sort?

A: Small arrays (< 50 elements) or nearly sorted data - very efficient



KEY POINTS:

✓ Different sorting algorithms have different time complexities

✓ Quick Sort is fastest in practice for average cases

✓ Merge Sort is stable and consistent O(n log n)

✓ Bubble Sort is simple but inefficient for large data

✓ Choose algorithm based on data size and type



IMPORTANT TERMS:

• Node: Each element in the tree

• Root: Top node

• Leaf: Node with no children

• Height: Longest path from root to leaf

• Traversal: Visiting all nodes in order

