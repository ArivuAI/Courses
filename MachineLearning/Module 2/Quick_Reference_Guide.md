# Module 2: Quick Reference Guide

## 🚀 Sequential Covering, FOIL, and EBL

---

## 📋 Sequential Covering Algorithm

### Pseudocode

```
function SEQUENTIAL_COVERING(Examples, Attributes, TargetAttr, TargetClass):
    LearnedRules = []
    RemainingExamples = Examples
    
    while positive examples remain in RemainingExamples:
        NewRule = LEARN_ONE_RULE(RemainingExamples, Attributes, TargetAttr, TargetClass)
        
        if NewRule.quality < threshold:
            break
        
        LearnedRules.append(NewRule)
        
        # Remove correctly covered positive examples
        RemainingExamples = RemainingExamples - CoveredBy(NewRule)
    
    return LearnedRules
```

### Learn-One-Rule (General-to-Specific)

```
function LEARN_ONE_RULE(Examples, Attributes, TargetAttr, TargetClass):
    Rule = {conditions: {}, prediction: TargetClass}
    
    while Rule.accuracy < threshold and Rule.coverage >= min_coverage:
        BestGain = -∞
        BestAttr = None
        BestValue = None
        
        for each Attribute in Attributes not in Rule.conditions:
            for each Value of Attribute:
                CandidateRule = Rule + (Attribute = Value)
                Gain = InformationGain(CandidateRule)
                
                if Gain > BestGain:
                    BestGain = Gain
                    BestAttr = Attribute
                    BestValue = Value
        
        if BestAttr is None:
            break
        
        Rule.conditions[BestAttr] = BestValue
    
    return Rule
```

### Key Characteristics

- **Search Strategy**: General-to-specific (start broad, add constraints)
- **Evaluation**: Information gain or accuracy improvement
- **Stopping Criteria**: Accuracy threshold or no improvement
- **Output**: Disjunctive set of rules (Rule1 OR Rule2 OR ...)

---

## 🔧 FOIL Algorithm

### Pseudocode

```
function FOIL(TargetPredicate, Predicates, PositiveExamples, NegativeExamples):
    LearnedRules = []
    Pos = PositiveExamples
    
    while Pos is not empty:
        NewRule = FOIL_LEARN_ONE_RULE(TargetPredicate, Predicates, Pos, NegativeExamples)
        LearnedRules.append(NewRule)
        Pos = Pos - CoveredBy(NewRule)
    
    return LearnedRules

function FOIL_LEARN_ONE_RULE(Target, Predicates, Pos, Neg):
    Rule = Target(x, y, ...) ←  # Initialize with target variables
    PosBindings = InitialBindings(Pos, Target)
    NegBindings = InitialBindings(Neg, Target)
    
    while NegBindings is not empty:
        Candidates = GENERATE_CANDIDATES(Rule, Predicates)
        BestLiteral = None
        BestGain = -∞
        
        for each Literal in Candidates:
            Gain = FOIL_GAIN(Literal, Rule, PosBindings, NegBindings)
            if Gain > BestGain:
                BestGain = Gain
                BestLiteral = Literal
        
        Rule = Rule + BestLiteral
        PosBindings = UpdateBindings(PosBindings, BestLiteral)
        NegBindings = UpdateBindings(NegBindings, BestLiteral)
    
    return Rule
```

### FoilGain Metric

```
FoilGain(L, Rule) = t × (log₂(p₁/(p₁+n₁)) - log₂(p₀/(p₀+n₀)))

Where:
    t  = number of positive bindings covered by Rule
    p₀ = positive bindings before adding literal L
    n₀ = negative bindings before adding literal L
    p₁ = positive bindings after adding literal L
    n₁ = negative bindings after adding literal L
```

### Three Types of Candidate Literals

**Type 1: New Predicate with Variables**
```
Q(v₁, v₂, ..., vᵣ)
```
- At least ONE variable must already exist in rule
- Can introduce NEW variables
- Example: `Parent(x, z)` where x exists, z is new

**Type 2: Equality Test**
```
Equal(xᵢ, xⱼ)
```
- Both variables must already exist in rule
- Tests if two objects are the same

**Type 3: Negations**
```
¬Q(...) or ¬Equal(...)
```
- Negation of Types 1 or 2
- Example: `¬Friend(x, z)`

### Example: Learning Grandparent(x, y)

```
Iteration 1:
    Rule: Grandparent(x, y) ←
    (Covers everything)

Iteration 2:
    Best literal: Parent(x, z)  [introduces variable z]
    Rule: Grandparent(x, y) ← Parent(x, z)
    (x is parent of someone)

Iteration 3:
    Best literal: Parent(z, y)  [completes chain]
    Rule: Grandparent(x, y) ← Parent(x, z) ∧ Parent(z, y)
    (x is parent of z, z is parent of y)
    ✓ Perfect accuracy!
```

---

## 🧬 Explanation-Based Learning (EBL)

### Three-Step Process

```
function EBL(TrainingExample, DomainTheory, TargetConcept):
    # Step 1: EXPLAIN
    ProofTree = EXPLAIN(TrainingExample, DomainTheory, TargetConcept)
    
    # Step 2: ANALYZE
    GeneralConditions = ANALYZE(ProofTree)
    
    # Step 3: REFINE
    OperationalRule = REFINE(GeneralConditions)
    
    return OperationalRule
```

### Step 1: EXPLAIN

Build a proof tree showing why the example satisfies the target concept.

```
Example: SafeToStack(Obj1, Obj2)

Proof Tree:
    SafeToStack(Obj1, Obj2)
        ↓ [Rule: SafeToStack(x,y) ← Lighter(x,y)]
    Lighter(Obj1, Obj2)
        ↓ [Rule: Lighter(x,y) ← Weight(x,wx) ∧ Weight(y,wy) ∧ wx < wy]
    Weight(Obj1, 5) ∧ Weight(Obj2, 12) ∧ 5 < 12
        ↓ [Rule: Weight(x,w) ← Volume(x,v) ∧ Density(x,d) ∧ w = v×d]
    Volume(Obj1, 10) ∧ Density(Obj1, 0.5) ∧ 5 = 10×0.5
    ∧ Volume(Obj2, 20) ∧ Density(Obj2, 0.6) ∧ 12 = 20×0.6
    ∧ 5 < 12
        ↓
    TRUE ✓
```

### Step 2: ANALYZE

Extract the weakest preimage (most general conditions).

```
Replace specific values with variables:
    Obj1 → x
    Obj2 → y
    10, 0.5, 5 → vx, dx, (vx × dx)
    20, 0.6, 12 → vy, dy, (vy × dy)

Weakest Preimage:
    "For ANY x and y where (vx × dx) < (vy × dy)"
```

### Step 3: REFINE

Create operational rule.

```
Learned Rule:
    SafeToStack(x, y) ← 
        Volume(x, vx) ∧ Density(x, dx) ∧
        Volume(y, vy) ∧ Density(y, dy) ∧
        (vx × dx) < (vy × dy)

Operational: Direct computation, no intermediate reasoning!
```

### Perfect Domain Theory

A domain theory is **perfect** if:
1. **Correct**: Every assertion is TRUE
2. **Complete**: Every positive example can be proven

Examples:
- Chess legal move rules ✓
- Physics laws (F=ma) ✓
- Logic circuit behaviors ✓

### The EBL Paradox

**Question**: "If we have perfect knowledge, why learn?"

**Answer**: Transform deep, slow knowledge into fast operational rules.

```
BEFORE EBL:
    SafeToStack → Lighter → Weight → Volume×Density
    (3-step reasoning chain, slow)

AFTER EBL:
    SafeToStack → Direct check: vx×dx < vy×dy
    (1-step, fast!)
```

---

## 📊 Comparison Table

### Sequential Covering vs Decision Trees

| Aspect | Sequential Covering | Decision Trees |
|--------|-------------------|----------------|
| Learning Style | One rule at a time | All rules simultaneously |
| Rule Independence | Independent rules | Shared structure |
| Natural Form | Disjunctive (OR) | Conjunctive (AND) |
| Modification | Easy to add/remove rules | Must rebuild tree |
| Explainability | Very high | High |

### Inductive vs Analytical Learning

| Aspect | Inductive | Analytical (EBL) |
|--------|-----------|------------------|
| Input | Data + Hypothesis space | Data + Hypothesis space + **Domain theory** |
| Sample Complexity | High (many examples) | Low (few examples) |
| Novelty Discovery | Can find new patterns | Reformulates existing knowledge |
| Guarantee | Statistical | Deductive (if theory correct) |
| Explainability | Often black box | Fully explainable |
| Robustness | Handles noise well | Sensitive to theory errors |

### FOIL vs Propositional Rules

| Aspect | Propositional | First-Order (FOIL) |
|--------|--------------|-------------------|
| Variables | No | Yes |
| Expressiveness | Single objects | Relationships between objects |
| Generalization | One rule per instance type | One rule for infinite instances |
| Recursion | No | Yes |
| Example | `age > 65 → senior` | `Grandparent(x,y) ← Parent(x,z) ∧ Parent(z,y)` |

---

## 💡 Quick Tips

### When to Use Sequential Covering
✓ Need explainable rules  
✓ Domain experts must validate  
✓ Regulatory compliance  
✓ Disjunctive concepts  

### When to Use FOIL
✓ Relational data (databases, graphs)  
✓ Complex relationships between objects  
✓ Need recursive rules  
✓ Knowledge graph reasoning  

### When to Use EBL
✓ Limited training data  
✓ Strong domain theory available  
✓ Need fast operational rules  
✓ Correctness is critical  

### When NOT to Use Rule-Based Learning
✗ High-dimensional perceptual data (images, audio)  
✗ Complex non-linear patterns  
✗ Massive datasets where interpretability not needed  
✗ No good domain theory (for EBL)  

---

## 🔑 Key Formulas

### Information Gain
```
Gain(S, A) = Entropy(S) - Σ(|Sᵥ|/|S|) × Entropy(Sᵥ)

Entropy(S) = -Σ pᵢ log₂(pᵢ)
```

### FoilGain
```
FoilGain(L, Rule) = t × (log₂(p₁/(p₁+n₁)) - log₂(p₀/(p₀+n₀)))
```

### Rule Accuracy
```
Accuracy = (Correctly Covered Examples) / (Total Covered Examples)
```

### Rule Coverage
```
Coverage = Number of examples matching rule conditions
```

---

## 📚 Study Checklist

- [ ] Understand sequential covering outer loop
- [ ] Implement learn-one-rule (general-to-specific)
- [ ] Explain difference from decision trees
- [ ] Describe three types of FOIL literals
- [ ] Calculate FoilGain for candidate literals
- [ ] Understand variable bindings in FOIL
- [ ] Walk through EBL three steps
- [ ] Explain the EBL paradox
- [ ] Compare inductive vs analytical learning
- [ ] Choose appropriate method for given problem

---

## 🎯 Common Pitfalls

1. **Confusing sequential covering with decision trees**
   - Sequential: Rules learned independently
   - Decision trees: Rules share structure

2. **Forgetting to remove covered examples**
   - Must remove after each rule in sequential covering
   - Otherwise, same rule learned repeatedly

3. **Misunderstanding FoilGain**
   - Accounts for variable bindings, not just examples
   - One example can create multiple bindings

4. **Thinking EBL discovers new knowledge**
   - EBL reformulates existing knowledge
   - Cannot learn what's not in domain theory

5. **Using rule-based learning for wrong domains**
   - Not suitable for high-dimensional perceptual data
   - Deep learning better for images, audio

---

## 📖 Further Reading

- Mitchell, T. (1997). *Machine Learning*. Chapters 10-11
- Quinlan, J.R. (1990). "Learning Logical Definitions from Relations"
- DeJong, G. & Mooney, R. (1986). "Explanation-Based Learning"

---

**Quick Reference Complete! Use this guide for rapid review and exam preparation.** 🌟

