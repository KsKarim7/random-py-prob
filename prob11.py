# CSE111 Fall-22(final question)
# question 02
class Mobile:
    countryCodes = {"880": "Bangladesh", "966": "India",
                    "455": "USA"}

    def __init__(self, model, simCardStatus):
        self.model = model
        self.__simCardStatus = simCardStatus
        print(f"Model {model} is manufactured.")

    def setSimCardStatus(self, status):
        self.__simCardStatus = status
        print("SIM card status updated successfully.")

    def getSimCardStatus(self):
        return self.__simCardStatus

    def __str__(self):
        return f"Mobile Phone Detail:\nModel:{self.model}\nSIM Card Status: {self.__simCardStatus}"


class Nokia(Mobile):
    codeList = []

    def __init__(self, name, cStatus, balance=0):
        super().__init__(name, cStatus)

        self.balance = balance
        self.cStatus = cStatus
        self.dialCallHistory = []

    def __str__(self):
        return f'Mobile Phone Detail: \nModel: {self.model} \nSIM Card Status: {self.cStatus} \nBalance: {self.balance} TK'

    def dialCall(self, num):
        # for k, v in super().countryCodes.items():
        #     if (k in super().countryCodes):
        #         break
        #     else:
        #         Nokia.codeList.append(k)
        # for i in Nokia.codeList:
        #     if (self.cStatus == True):
        #         pass
        #         if (i in Nokia.codeList):
        #             if (self.balance != 0):
        #                 if (num not in self.dialCallHistory):
        #                     self.dialCallHistory.append(num)
        #                 return f'Dialling the number {num} to {super().countryCodes[i]} region'
        #             else:
        #                 return "Insufficient balance!"
        #                 # break;
        #         else:
        #             return f'Dialling is not allowed in this region'
        #     else:
        #         return 'No SIM card available'
        if (self.cStatus == True):
            if (self.balance > 0):
                for k, v in super().countryCodes.items():
                    if (k in num):
                        self.dialCallHistory.append(num)
                        return f'Dialling the number {num} to {v} region'
                else:
                    return 'Dialing is not allowed in this region'
            else:
                return 'Insufficient Balance'
        else:
            return 'No Sim card available'

    def changeSIMCardStatus(self):
        self.cStatus = True
        print("SIM card status updated successfully.")

    def rechargeSIMCard(self, tk):
        self.balance += tk
        print(f'Recharge successful! Current balance {self.balance} TK.')


N3110 = Nokia("N3110", False)
print("#######################################")
print(N3110)
print("1======================================")
N1100 = Nokia("N1100", True, 100)
print("#######################################")
print(N1100)
print("2======================================")
print(N3110.dialCall("88017196xxxx"))
print("3======================================")
N3110.changeSIMCardStatus()
print("4======================================")
print(N3110.dialCall("88017196xxxx"))
print("5======================================")
N3110.rechargeSIMCard(200)
print("6======================================")
print(N3110.dialCall("88017196xxxx"))
print("7======================================")
print(N1100.dialCall("45617196xxxx"))
print("8======================================")
print(N1100.dialCall("45517196xxxx"))
print(N1100.dialCall("96617196xxxx"))
print("9======================================")
print(f"Dial call history for {N1100.model}:{N1100.dialCallHistory}")
print(f"Dial call history for {N3110.model}:{N3110.dialCallHistory}")
