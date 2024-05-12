import re

def extract_qa_tuples(text):
    pattern = r'\*\*QUESTION:\*\*\s*((?:.|\n)*?)\s*\*\*ANSWER:\*\*\s*((?:.|\n)*?)(?=\s*\*\*QUESTION:\*\*|\Z)'
    matches = re.findall(pattern, text + "\n\n**QUESTION:**", re.DOTALL) # The addition is a hack to get around the tricky lookahead problem
    return [(question.strip(), answer.strip()) for question, answer in matches]


text_string_1 = """**QUESTION:**
What causes the errors:
```
error while loading shared libraries: libgomp.so.1: No such file or directory
error while loading shared libraries: libz.so: No such file or directory
```
When running `./verusd` on a Linux Distro?

**ANSWER:**
These errors may be caused by required dependencies for `./verusd` not being installed by default on a Linux distribution. The lack of required dependencies results in the error messages when you try to run `./verusd`. 

**QUESTION:**
If you run `./verusd` and encounter these errors:
```
error while loading shared libraries: libgomp.so.1: No such file or directory
error while loading shared libraries: libz.so: No such file or directory
```
How do you solve them?

**ANSWER:**
In order to solve these errors, which are likely caused by dependencies not being installed by default on a Linux distro, try the following:

1. **Install the libgomp and zlib1g-dev libaries.** This can be accomplished by running `sudo apt-get install libgomp1 zlib1g-dev`.

2. Try running the command `./verusd` again and see if installing the dependencies worked."""

text_string_2 = """**QUESTION:**
What are VerusIDs?

**ANSWER:**
VerusIDs are a fully-functional blockchain protocol. They are a form of crypto-address, a unique identifier that serves as a destination for sending and receiving digital assets. Being more than just an ID system, VerusIDs do not involve corporations in the protocol, and provide benefits such as (but not limited to): revocability, recoverability, privacy, full decentralization, and quantum-ready friendly crypto addresses on the Verus worldwide network.

**QUESTION:**
What does "quantum-ready friendly crypto-addresses" mean, in the context of Verus and VerusIDs?

**ANSWER:**
The phrase "quantum-ready friendly crypto-addresses," in the context of Verus and VerusIDs, refers to the resistance of VerusIDs against attack by quantum computers that use existing algorithms. Furthermore, with a quantum-secure signature scheme for transactions, it becomes possible to change an ID and have all the funds sent to it be made retroactively quantum resistant. Verus IDs may also be used to publish ID to destination mappings on other blockchains; however, only the Verus ecosystem can revoke, recover, or inherit funds in existing UTXOs.

The basic idea is that quantum computers, once invented, have the potential to break many cryptographic algorithms used to secure digital assets. Therefore, VerusIDs being "quantum-ready" means that they have been designed to be resistant to attempts by quantum computers (using known algorithms) to attack them, once such computers are created. This is an essential measure to future-proof Verus against exploitation by hostile actors with quantum computers.

**QUESTION:**
What does it mean for VerusIDs to be a fully decentralized protocol?

**ANSWER:**
VerusIDs can be created by anyone, without needing permission from a central authority, and give their creator complete, self-sovereign control over their ID. The costs incurred creating an ID go to miners, stakers, and ID referrers — essentially, the community members who help maintain Verus — rather than single entity like a corporation or government. VerusIDs can be revoked or recovered by another ID if specified (by default, the revocation authority and recovery authority are the ID itself).

Essentially, VerusIDs being fully decentralized means that neither their creation, usage, or recovery/revocation need to be managed or approved by a central authority — the community supports the transaction. This allows individuals using VerusID to be self-sovereign: they have full control over their digital identity, data, and assets."""

print(extract_qa_tuples(text_string_2))