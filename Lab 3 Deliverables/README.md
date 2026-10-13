# Lab 3 Deliverables – Component Modelling & Architectural Pattern Selection

**Aryan Upadhyay · PES1UG25CS806 · Section C**
**Problem Statement #60 – Podcast Guest Scheduling & Outline Builder**

| # | Deliverable | Files |
|---|-------------|-------|
| 1 | **Component Diagram** – Layered architecture (Presentation / Business / Data); 6 components (Web Portal, Booking Manager, Outline Manager, Calendar Integration, Run-of-Show Generator, Episode Repository) + Calendar API, Object Storage, Episode Database; 9 interfaces in ball (provided) / socket (required) notation, labelled with protocol; numbered data flows (booking 1-5, run-of-show A-D) | `Lab3_Component_Diagram.png`, `Lab3_Component_Diagram.pdf`, `Lab3_Component_Diagram.drawio` (editable in draw.io) |
| 2 | **Written Justification** (1 page) – "We chose a Layered Architecture for the Podcast Guest Scheduling & Outline Builder System": scenario review, style comparison (Layered / Microservices / Client-Server), two reasons, security advantage, performance benefit | `Lab3_Architecture_Justification.docx`, `Lab3_Architecture_Justification.pdf` |

The handout's example components map to this scenario as Order Manager → **Booking Manager** and Payment Service → **Calendar Integration** (given interface Order Manager ↔ Payment Service → Booking Manager ↔ Calendar Integration, `ICalendarSync`).
