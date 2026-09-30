from llm import get_llm


class SimpleAgent:
    def __init__(self):
        self.llm = get_llm()

    def invoke(self, payload, config=None):
        if isinstance(payload, dict):
            user_input = payload.get("user_input", "")
        else:
            user_input = str(payload)

        trace = [
            {"node": "entrada", "detail": "Mensagem recebida"},
            {"node": "llm", "detail": "Resposta gerada"},
            {"node": "fim", "detail": "Concluído"},
        ]

        try:
            response = self.llm.invoke(user_input)
            final_answer = getattr(response, "content", str(response))
        except Exception as exc:
            final_answer = f"Erro ao chamar o modelo: {exc}"

        return {
            "final_answer": final_answer,
            "trace": trace,
            "subgraph": {"nodes": {}, "edges": [], "center_ids": []},
        }


def build_agent():
    return SimpleAgent()
