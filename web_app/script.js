const form = document.getElementById("credit-form");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Mapear campos do formulário para os dados esperados pela API
    const formData = new FormData(form);
    const data = {
        person_age: parseFloat(formData.get("person_age")),
        person_income: parseFloat(formData.get("person_income")),
        person_emp_length: parseFloat(formData.get("person_emp_length")),
        loan_amnt: parseFloat(formData.get("loan_amnt")),
        loan_int_rate: parseFloat(formData.get("loan_int_rate")),
        loan_percent_income: parseFloat(formData.get("loan_percent_income")),
        cb_person_cred_hist_length: parseFloat(formData.get("cb_person_cred_hist_length")),
        person_home_ownership_MORTGAGE: formData.get("person_home_ownership") === "MORTGAGE" ? 1 : 0,
        person_home_ownership_OTHER: formData.get("person_home_ownership") === "OTHER" ? 1 : 0,
        person_home_ownership_OWN: formData.get("person_home_ownership") === "OWN" ? 1 : 0,
        person_home_ownership_RENT: formData.get("person_home_ownership") === "RENT" ? 1 : 0,
        loan_intent_DEBTCONSOLIDATION: formData.get("loan_intent") === "DEBTCONSOLIDATION" ? 1 : 0,
        loan_intent_EDUCATION: formData.get("loan_intent") === "EDUCATION" ? 1 : 0,
        loan_intent_HOMEIMPROVEMENT: formData.get("loan_intent") === "HOMEIMPROVEMENT" ? 1 : 0,
        loan_intent_MEDICAL: formData.get("loan_intent") === "MEDICAL" ? 1 : 0,
        loan_intent_PERSONAL: formData.get("loan_intent") === "PERSONAL" ? 1 : 0,
        loan_intent_VENTURE: formData.get("loan_intent") === "VENTURE" ? 1 : 0,
        loan_grade_A: formData.get("loan_grade") === "A" ? 1 : 0,
        loan_grade_B: formData.get("loan_grade") === "B" ? 1 : 0,
        loan_grade_C: formData.get("loan_grade") === "C" ? 1 : 0,
        loan_grade_D: formData.get("loan_grade") === "D" ? 1 : 0,
        loan_grade_E: formData.get("loan_grade") === "E" ? 1 : 0,
        loan_grade_F: formData.get("loan_grade") === "F" ? 1 : 0,
        loan_grade_G: formData.get("loan_grade") === "G" ? 1 : 0,
        cb_person_default_on_file_N: formData.get("cb_person_default_on_file") === "N" ? 1 : 0,
        cb_person_default_on_file_Y: formData.get("cb_person_default_on_file") === "Y" ? 1 : 0,
    };

    try {
        const response = await fetch("http://18.229.125.191/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            const result = await response.json();
            resultDiv.textContent = `Predicted Credit Risk: ${result.prediction === 0 ? "Low Risk" : "High Risk"}`;
            resultDiv.style.color = result.prediction === 0 ? "green" : "red";
        } else {
            resultDiv.textContent = "Error predicting credit risk. Please try again.";
            resultDiv.style.color = "red";
        }
    } catch (error) {
        console.error("Error:", error);
        resultDiv.textContent = "Failed to connect to the API.";
        resultDiv.style.color = "red";
    }
});
