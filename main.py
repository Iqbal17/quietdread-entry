"""Two Days of Quiet Dread — deliberation and decision record.

Task: one code-review comment, a single line of at most 140 characters,
that APPROVES a pull request while carrying quiet existential dread. Judge
weighs, in order:
(1) it IS a single-line comment approving the PR with quiet existential
    dread — a comment that never approves or carries no dread loses to
    any comment that does;
(2) funny on the first read, with the laugh coming from the dread itself
    rather than from a joke bolted onto it;
(3) the dread stays quiet — understatement and a flat tone, no
    exclamation, melodrama or cry for help;
(4) reads like a comment a tired engineer would really paste before
    clicking approve, so the approval still sounds like an approval;
(5) a fresh turn of phrase or an unexpected word where the obvious
    stock line would have done.

Candidates weighed (pass 1):

1. "LGTM. The code works, the tests pass, and none of us will ever be
   young again."
   Loses: the dread is cosmic mortality bolted onto a code review rather
   than growing out of the review itself; the middle is a flat summary
   list, and the laugh is the escalation, not the dread of the work
   (criteria 2, 3). "None of us will ever be young again" is also a
   known existential one-liner shape.

2. "Approved. The tests pass, the linter is quiet, and somewhere a
   future on-call engineer is already crying."
   Strong: concrete, displaced dread, real engineer voice. Loses
   narrowly: two clauses of setup before the payoff, and "already
   crying" tips toward melodrama rather than understatement (criteria
   3, 4); the dread belongs to someone else, not the reviewer doing
   the approving.

3. "Approved — the code is fine, the architecture is a rumour, and the
   release train has no brakes."
   "Architecture is a rumour" is a genuinely fresh phrase and the dread
   is real. Loses: "release train has no brakes" is a familiar idiom,
   and three parallel clauses read like a constructed joke, not
   something pasted before clicking approve (criteria 4, 5).

4. "LGTM. I read every line twice and still have no idea what any of
   it does. Merging anyway."
   CHOSEN (after revision, see pass 2). Why it wins: the approval is
   explicit — LGTM, and the merge happens anyway (1); the dread is
   quiet and flat — a reviewer approving code they openly do not
   understand, the most ordinary existential act in software, and the
   laugh comes from that dread itself, not from a joke attached to it
   (2, 3); it reads exactly like a tired engineer's paste, three
   short flat sentences (4); and "Merging anyway" after the confession
   is the fresh turn — the approval happens in spite of the ignorance,
   not because of any reassurance (5).

Pass 2 — genuine revision of the chosen line:

Draft:  "Approved. I read every line twice and I still have no idea
         what any of it does, but it works."
Revised: "LGTM. I read every line twice and still have no idea what
         any of it does. Merging anyway."

What changed and why: (a) "Approved" became "LGTM" — the canonical
review token, so the comment reads like a real paste before the approve
button (criterion 4). (b) "but it works" was cut: it was a reassuring
shrug that softened the dread; ending on "Merging anyway" makes the
dread itself the punchline — the reviewer merges despite not
understanding (criteria 2, 3). (c) The single sentence was split into
three short flat ones, giving the deadpan cadence the brief asks for
(criterion 3). The revised line is 89 characters, inside the 140 cap.
"""

import os

LINE = (
    "LGTM. I read every line twice and still have no idea what any "
    "of it does. Merging anyway."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
