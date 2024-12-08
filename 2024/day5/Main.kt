package day5

import common.readInput

const val INPUT_FILE = "2024/day5/input.txt"

fun <T> List<T>.splitAt(index: Int) = subList(0, index) to subList(index + 1, size)
fun <T> List<T>.middle() = this[size / 2]

fun main() {
    val input = readInput(INPUT_FILE)
    val (rules, pages) = input.splitAt(input.indexOfFirst { it.isEmpty() })

    val dependency = mutableMapOf<Long, MutableList<Long>>()
    rules.forEach { (before, after) -> dependency.getOrPut(after) { mutableListOf() }.add(before) }

    val (part1, part2) = pages.map { page ->
        val valid = page.zipWithNext { a, b -> b !in dependency[a]!! }.all { it }
        val ordered = page.sortedWith { a, b -> if (a in dependency[b]!!) -1 else 1 }
        (if (valid) page.middle() else 0) to (if (valid) 0 else ordered.middle())
    }.unzip().run { first.sum() to second.sum() }

    println("Part 1: $part1")
    println("Part 2: $part2")
}