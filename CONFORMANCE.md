# IEEE Std 1788-2015 Conformance Document

This document details the configuration, capabilities, and compliance attributes of this Python-based Interval Arithmetic library, satisfying the official documentation requirements set forth in Section 4 of the IEEE Std 1788-2015 specification.

---

## 1. Scope and Implementation Flavor
This library provides a complete, operational implementation of **Flavor 1: Set-Based Interval Arithmetic**. 
* **Mathematical Foundation:** Intervals are defined as closed sets of connected real numbers $[a, b] = \{ x \in \mathbb{R}^* \mid a \le x \le b \}$, operating over the extended real numbers $\mathbb{R}^* = \mathbb{R} \cup \{-\infty, +\infty\}$.
* **Compliance Level:** Fully implements both the **Level 1** (Bare Intervals) arithmetic/relational layer and the **Level 2** (Decorated Intervals) state-tracking context layer.

---

## 2. Representation and Core Types

### 2.1 Bare Intervals (`Interval` Class)
* **Datatype Coercion:** Bound representations (`self.lo` and `self.hi`) are explicitly cast to arbitrary-precision floating-point numbers (`mpfr`) using the `gmpy2` numeric computational backend.
* **Special Interval States:**
  * **Empty Interval ($\emptyset$):** Triggered naturally by any operation causing domain collapse ($lo > hi$). Formally initialized via `Interval.empty()`, exposing properties `is_empty = True`, and serialized as `[empty]`.
  * **Entire Interval ($\mathbb{R}^*$):** Spans the entire real number line from negative to positive infinity. Formally initialized via `Interval.entire()`, exposing properties `is_entire = True`, and serialized as `[entire]`.

### 2.2 Decorated Intervals (`DecoratedInterval` Class)
* **State Tracking:** Pairs an underlying `Interval` box with a historical tracking token to communicate mathematical continuity and domain validity across chains of calculations.
* **Supported Decoration Hierarchy:**
  * `COM` (Common): Bounded, non-empty, and continuous.
  * `DAC` (Defined and Bounded-state Contained): Bounded and non-empty, but the global domain scope boundary has been breached (e.g., evaluating $[-\infty, \infty]$).
  * `DEF` (Defined): Non-empty, but sequence properties or bounded-state criteria have degraded.
  * `TRV` (Trivial): Assigned automatically to any valid operation evaluating to the empty set (`[empty]_trv`).
  * `ILL` (Ill-formed / NaI): Indicates an invalid numerical or logical sequence. Instantiated via `DecoratedInterval.new_nai()`, setting `nai = True`, and serialized as `[NaI]`.

---

## 3. Precision Settings & Directed Rounding
To guarantee strict mathematical containment ($x \in [\underline{x}, \overline{x}]$), all numerical computations isolate and control processor rounding behaviors explicitly via `gmpy2` context managers:
* **Lower Bound Evaluation:** Enforces strict rounding down towards negative infinity (`RoundDown`).
* **Upper Bound Evaluation:** Enforces strict rounding up towards positive infinity (`RoundUp`).
* **Set Metrics Evaluation:** Point-metrics like `width` and `radius` enforce `RoundUp` tracking to ensure precision errors err on the side of caution. Point-metrics like `midpoint` use round-to-nearest (`RoundNearest`) mechanics as specified by the standard.

---

## 4. Operational Capability Matrix

| Operation Category | Implemented Functions / Methods | IEEE 1788 Section |
| :--- | :--- | :--- |
| **Primitives** | `+`, `-`, `*`, `/`, `neg`, `abs` | Section 8.2 & 8.3 |
| **Transcendental Math** | `sin`, `cos`, `tan`, `sinh`, `cosh`, `tanh`, `asin`, `acos`, `atan`, `asinh`, `acosh`, `atanh`, `atan2` | Section 8.4 |
| **Set Metrics** | `width`, `radius`, `midpoint`, `magnitude`, `mignitude`, `inf_sub`, `sup_sub` | Section 8.5 |
| **Set Relations** | `contains`, `subset`, `proper_subset`, `overlaps`, `disjoint`, `precedes`, `meets` | Section 8.6 |
| **Boolean Queries** | `is_empty`, `is_entire`, `is_common`, `is_bounded`, `is_point`, `is_nai` | Section 8.7 |
| **Utility** | `bisect`, `intersection`, `hull`, `from_string` | Section 8.2 & 11.2 |

---

## 5. Textual Serialization and Parsing
* **String Generation (`__str__`):** Text mapping exactly isolates special cases into exact literal matches (`[empty]`, `[entire]`, `[NaI]`), while computing standard boxes using lowercase decoration tags (e.g., `[1.5, 2.0]_com`).
* **Exact String Parsing (`from_string`):** The input parser isolates incoming string constants via regular expressions and runs boundary construction dynamically inside `RoundDown` and `RoundUp` precision blocks to avoid binary approximation leaks on raw decimal strings (e.g., correctly expanding `0.1` to tightly bracket $1/10$).
