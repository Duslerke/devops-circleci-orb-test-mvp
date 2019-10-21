#!/usr/bin/env bats

@test "just a test" {
  result="$(expr 2 + 2 )"
  [ "$result" -eq 4 ]
}
