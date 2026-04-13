from flask import Flask, render_template

app = Flask(__name__)

mamlakatlar = ["Xitoy", "Rossiya", "Germaniya", "Fransiya", "Braziliya", "Hindiston", "Misr"]

@app.route("/mamlakatlar/<int:i>/qo'shni")
def qoshni_mamlakat(i):
    if 0 <= i < len(mamlakatlar):
        mamlakat = mamlakatlar[i]

        oldingi = mamlakatlar[i-1] if i > 0 else None
        keyingi = mamlakatlar[i+1] if i < len(mamlakatlar)-1 else None

        return render_template(
            'qoshni.html',
            mamlakat=mamlakat,
            oldingi=oldingi,
            keyingi=keyingi
        )
    else:
        return "Noto'g'ri indeks ❌"

if __name__ == "__main__":
    app.run(debug=True)
